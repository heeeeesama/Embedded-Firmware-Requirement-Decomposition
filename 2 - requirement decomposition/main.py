import os
import json
import argparse
import logging
import datetime
import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
from multiprocessing.pool import ThreadPool
from tqdm import tqdm
from eval import acc_score, F1_scorer, compute_exact, eval_asqa, eval_bmcqa, acc_choice
from utils import seed_everything
import requests
import re
from compare import NoteQualityEvaluator


parser = argparse.ArgumentParser()
parser.add_argument(
    "--mode",
    type=str,
    choices=["eval", "interactive"],
    default="eval",
    help="Run mode: eval for batch evaluation or interactive for manual Q&A",
)
parser.add_argument(
    "--model",
    type=str,
    choices=[
        "qwen3-235b"
        "qwen3-32b",
        "qwen3-8b",
    ],
    default="qwen3-8b",
    help="Model to use",
)
parser.add_argument(
    "--max_step", type=int, default=3, help="Maximum number of update steps"
)
parser.add_argument(
    "--max_fail_step", type=int, default=2, help="Maximum number of failed steps"
)
parser.add_argument(
    "--MaxClients", type=int, default=1, help="Number of concurrent clients"
)
parser.add_argument(
    "--retrieve_top_k",
    type=int,
    default=5,
    help="Number of documents to retrieve per query",
)
parser.add_argument(
    "--max_top_k",
    type=int,
    default=15,
    help="Total maximum number of documents to retrieve",
)
parser.add_argument(
    "--dataset",
    type=str,
    choices=[
        "bmcqa",
    ],
    default="bmcqa",
    help="Dataset to use",
)
#已完成
parser.add_argument(
    "--method",
    type=str,
    default="miki",
    choices=["mapping_miki", "miki", "base", "mapping_base", "base_wo_retri", "mapping_base_wo_retri"]
)
parser.add_argument(
    "--resume_path",
    type=str,
    default="",
    help="Path to the file for resuming generation",
)
parser.add_argument(
    "--retrieve_method",
    type=str,
    default="emb",
    help="Retrieval method to use",
)
parser.add_argument(
    "--device", type=str, default="cuda:0", help="Device to run inference on"
)
args = parser.parse_args()


# Ollama服务配置
OLLAMA_HOST = "http://localhost:11434/api/generate"

# 创建一个全局变量来跟踪Token使用情况
total_token_usage = {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0
}


def split_text_by_tags(input_str):
    # 查找起始标签位置
    start_index = input_str.find("<think>")
    if start_index == -1:
        return "", input_str  # 未找到起始标签的情况

    # 在剩余文本中查找结束标签
    end_index = input_str.find("</think>", start_index)
    if end_index == -1:
        # 未找到结束标签时截取到字符串末尾
        return input_str[start_index:], ""

    # 计算结束标签的终止位置（包含标签本身）
    end_tag_end = end_index + len("</think>")

    # 分割字符串
    part1 = input_str[start_index:end_tag_end]  # 包含完整标签
    part2 = input_str[end_tag_end:]  # 剩余内容

    return part1, part2

def call_llm_template(template, variables):
    """使用Ollama调用模板化提示"""
    template_text = load_template(template)
    if not template_text:
        return ""

    prompt_text = template_text.format(**variables)
    return call_ollama(prompt_text)

def load_template(template_name, language="ch"):
    """加载提示模板文件"""
    template_path = f"../prompts/{language}/{template_name}"
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"警告: 模板文件 {template_path} 不存在")
        return ""
    except Exception as e:
        print(f"读取模板错误: {str(e)}")
        return ""

def call_ollama(prompt_text, system_prompt=None):
    global total_token_usage  # 声明使用全局变量

    # =================== 原有的Ollama调用逻辑 ===================
    if args.model == "qwen3-8b":
        messages = []

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({"role": "user", "content": prompt_text})

        # 格式化Qwen对话模板
        def format_qwen3_messages(messages):
            formatted = []
            for msg in messages:
                if msg["role"] == "system":
                    formatted.append(f"<|im_start|>system\n{msg['content']}<|im_end|>")
                elif msg["role"] == "user":
                    formatted.append(f"<|im_start|>user\n{msg['content']}<|im_end|>")
                elif msg["role"] == "assistant":
                    formatted.append(f"<|im_start|>assistant\n{msg['content']}<|im_end|>")
            formatted.append("<|im_start|>assistant\n")
            return "\n".join(formatted)

        full_prompt = format_qwen3_messages(messages)

        # 构造请求数据
        if args.model == "qwen3-8b":
            data = {
                "model": "qwen3:8b",
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "top_p": 0.9,
                    "num_predict": 2000
                }
            }

        # 发送请求
        try:
            response = requests.post(
                OLLAMA_HOST,
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
                timeout=120
            )
            response.raise_for_status()
            response_data = response.json()

            # Ollama API返回的Token信息在 'prompt_eval_count' 和 'eval_count' 字段
            prompt_tokens = response_data.get("prompt_eval_count", 0)
            completion_tokens = response_data.get("eval_count", 0)

            # 更新Token计数器
            total_token_usage["prompt_tokens"] += prompt_tokens
            total_token_usage["completion_tokens"] += completion_tokens
            total_token_usage["total_tokens"] += prompt_tokens + completion_tokens

            return response_data.get("response", "").strip()
        except Exception as e:
            print(f"Ollama调用失败: {str(e)}")
            return ""
    else:
        print(f"不支持的模型: {args.model}")
        return ""

def get_context(data):
    """格式化检索结果作为上下文"""
    return "\n".join([
        f"Title: {d['title']}\nText: {d['text']}\n"
        for d in data
    ])

def save_log_to_file(logger, log_file="my_log", log_folder="logs"):
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    current_date = datetime.datetime.now().strftime("%Y%m%d-%H_%M_%S")
    log_file_name = f"{log_file}-{current_date}.log"
    log_file_name = re.sub(r'[:<>"|?*\\/]', '_', log_file_name)
    file_handler = logging.FileHandler(os.path.join(log_folder, log_file_name))
    logger.addHandler(file_handler)

def mapping_init_note(query, mapping, refs):
    think, note = split_text_by_tags(call_llm_template(
        "mapping_init_note", {"query": query, "mapping": mapping, "refs": refs}
    ))
    return note

def create_chain(query):
    think, note = split_text_by_tags(call_llm_template(
        "create_chain", {"query": query}
    ))
    return note


def mapping_gen_new_query(query, note, causal_chain, mapping, query_log):
    think, query = split_text_by_tags(call_llm_template(
        "mapping_gen_new_query", {
            "query": query, "note": note, "causal_chain": causal_chain, "mapping": mapping, "query_log": query_log
        }
    ))
    return query

def mapping_refine_note(note, query, mapping, refs, causal_chain):
    think, note = split_text_by_tags(call_llm_template(
        "mapping_refine_note",
        {"note": note, "query": query, "mapping": mapping, "refs": refs, "causal_chain": causal_chain}
    ))
    return note


def gen_answer(query, note_str):
    return call_llm_template("gen_answer", {"query": query, "note": note_str})

def retrieve_note_mapping(doc_id, query, mapping, answer, top_k=2):
    ref_log, llm_times, note_log, query_log, compare_log, query_list, chain_log = [], 0, [], [], [], [], []
    # 基于初始问题的首次top—k检索
    refs = retrieve(args.dataset, query=query, topk=top_k)
    # 初始化知识增量清单
    note = best_note = mapping_init_note(query, mapping, get_context(refs))
    # 构建因果链
    causal_chain = create_chain(query)
    chain_log.append({"chain": causal_chain})
    ref_log.append({"refs": refs, "step": 0, "flag": "init_refs"})
    note_log.append({"note": note, "step": 0, "flag": "init_note"})
    llm_times += 1
    step, notes_status = 0, []

    while step < args.max_step:
        # 收集所有已使用的参考文本
        all_refs = set()
        for log_entry in ref_log:  # 遍历每个日志条目
            for ref_doc in log_entry['refs']:  # 遍历每个日志条目中的文档列表
                title = ref_doc.get('title', '无标题')
                text = ref_doc.get('text', '无内容')
                all_refs.add(title + text)

        if len(all_refs) > args.max_top_k:
            break

        # 基于原始问题、子问题集、因果链、知识图谱与当前知识增量清单生成新子问题
        new_query = mapping_gen_new_query(query, best_note, causal_chain, mapping, str(query_list))

        #_, new_causal_chain, key_note_dict = parse_text_as_new_query(new_query)
        # 更新子问题清单
        #if len(new_causal_chain) > 0:
        query_list.append(new_query)

        llm_times += 1

        # 基于原始问题、子问题清单执行新top-k检索
        refs = retrieve(
            args.dataset, query=(new_query + "\n" + query)[:500], topk=top_k
        )

        # 过滤已使用的参考
        unique_refs = [
                          r for r in refs
                          if (r['title'] + r['text']) not in all_refs
                      ][:args.retrieve_top_k]

        if not unique_refs:
            unique_refs = refs[:args.retrieve_top_k]

        # 基于原始问题、当前轮次检索资料、知识图谱与当前知识增量清单生成候选知识增量清单
        note = mapping_refine_note(best_note, query, mapping, get_context(unique_refs), causal_chain).replace("\n", "")
        llm_times += 1

        # 比较知识增量清单质量
        evaluator = NoteQualityEvaluator(emb_model=emb_model)
        status = "False"
        detail = ""
        if len(best_note) > 0:
            status, detail = evaluator.compare_notes(query, best_note, note)
        else:
            best_note = note

        flag = "True" if status else "False"

        ref_log.append({"refs": unique_refs, "step": step, "flag": flag})
        note_log.append({"note": note, "step": step, "flag": flag})
        query_log.append({"query": new_query, "step": step, "flag": flag})
        compare_log.append({"compare": detail, "step": step, "flag": flag})

        if status:
            best_note = note

        notes_status.append(status)
        if notes_status.count(False) >= args.max_fail_step:
            break
        step += 1

    llm_times += 1
    return {
        "id": doc_id,
        "question": query,
        "answer": answer,
        "output": gen_answer(query, best_note),
        "miki": best_note,
        "chain_log": chain_log,
        "query_log": query_log,
        "note_log": note_log,
        "ref_log": ref_log,
        "compare_log": compare_log,
    }

def process_doc_cell(idx, doc_cell, args):
    id_new, query, mapping, answer = idx, doc_cell["question"], doc_cell["mapping"], doc_cell["answer"]

    if args.method not in ["miki", "mapping_miki"]:
        if args.dataset in ["bmcqa"]:
            gen_name = f"{args.method}_{args.dataset}"
        else:
            gen_name = args.method

        if args.method in ["base_wo_retri"]:
            params = {"query": query}
            output = call_llm_template(gen_name, params)
        elif args.method in ["mapping_base_wo_retri"]:
            params = {
                "query": query,
                "mapping": mapping
            }
            output = call_llm_template(gen_name, params)
        elif args.method in ["mapping_base"]:
            params = {
                "query": query,
                "mapping": mapping,
                "refs": get_context(
                    retrieve(args.dataset, query=query, topk=args.retrieve_top_k)
                ),
            }
            output = call_llm_template(gen_name, params)

        # base
        else:
            params = {
                "query": query,
                "refs": get_context(
                    retrieve(args.dataset, query=query, topk=args.retrieve_top_k)
                )
            }
            output = call_llm_template(gen_name, params)

        return {"id": id_new, "query": query, "answer": answer, "output": output}

    elif args.method in ["miki"]:
        return retrieve_note_mapping(id_new, query, " ", answer, top_k=args.retrieve_top_k)

    else:
        return retrieve_note_mapping(id_new, query, mapping, answer, top_k=args.retrieve_top_k)




if __name__ == "__main__":
    # 检查Ollama服务
    try:
        response = requests.get("http://localhost:11434", timeout=5)
        if response.status_code != 200:
            print("请先启动Ollama服务: ollama serve")
            exit(1)
    except:
        print("无法连接到Ollama服务，请确保ollama正在运行")
        exit(1)

    LAUGUAGE = "ch"
    seed_everything(66)

    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%m/%d/%Y %H_%M_%S",
        level=logging.INFO,
    )
    save_log_to_file(
        logger,
        log_file=f"{args.dataset}_{args.method}_{args.model}",
        log_folder="../log",
    )
    logger.info(f"{'*' * 30} CONFIGURATION {'*' * 30}")
    for key, val in sorted(vars(args).items()):
        keystr = "{}".format(key) + (" " * (30 - len(key)))
        logger.info("%s -->   %s", keystr, val)

    # 加载FAQ索引
    dataset_name = args.dataset
    vector_path = "./bmcqa corpus/BMC.index"
    vector = faiss.read_index(vector_path)

    emb_model = SentenceTransformer("../model/bge-m3", device='cpu')
    raw_data = pd.read_csv("../bmcqa corpus/bmc_chunks.tsv", sep="\t")

    def retrieve(_, query, topk):
        feature = emb_model.encode([query])
        _, match_id = vector.search(feature, topk)
        # 返回文档
        return [
            {
                "title": raw_data.iloc[i]["title"],
                "text": raw_data.iloc[i]["text"]
            }
            for i in match_id[0]
        ]


    formatted_time = datetime.datetime.now().strftime("%Y%m%d-%H_%M_%S")

    with open(f"./benchmark.json", encoding="utf-8") as f:
        qa_data = json.load(f)

    retrieve_method = args.retrieve_method

    save_path = f"./output/{args.dataset}/{retrieve_method}/{args.method}/{args.model}"
    os.makedirs(save_path, exist_ok=True)

    all_result = []

    if args.resume_path:
        with open(args.resume_path, "r", encoding="utf-8") as fin:
            resume_data = [json.loads(i) for i in fin.readlines()]
            all_result = resume_data
            filepath = args.resume_path
    else:
        resume_data = []
        filepath = (
            f"{save_path}/topk-{args.retrieve_top_k}-{formatted_time}.jsonl"
            if args.method not in ["miki", "mapping_miki"]
            else f"{save_path}/topk-{args.retrieve_top_k}__max_step-{args.max_step}__max_fail_step-{args.max_fail_step}-{formatted_time}.jsonl"
        )
    logger.info(f"问答实验结果将保存在：'{filepath}'.")

    total_token_usage = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0
    }

    last_id = len(resume_data)
    batch_size = args.MaxClients
    logger.info("开始问答实验...")
    print("len(qa_data):", len(qa_data))
    for i in tqdm(range(last_id, len(qa_data), batch_size)):
        pool = ThreadPool(processes=args.MaxClients)
        current_batch = qa_data[i: i + batch_size]
        tasks = [
            (idx + i, doc_cell, args) for idx, doc_cell in enumerate(current_batch)
        ]
        print("task:", tasks)

        #process_doc_cell开始实验 传参tasks
        results = pool.starmap(process_doc_cell, tasks)
        pool.close()
        pool.join()

        for result in results:
            if result:
                all_result.append(result)
                with open(filepath, "a", encoding="utf-8", buffering=1) as fout:
                    fout.write(json.dumps(result, ensure_ascii=False) + "\n")

    logger.info("开始评估...")

    predictions = [data["output"] for data in all_result]
    answers = [data["answer"] for data in all_result]

    if "bmcqa" in args.dataset:
        eval_result = eval_bmcqa(all_result, emb_model)
    else:
        eval_result = eval_asqa(all_result)

    if eval_result:
        with open(filepath, "a", encoding="utf-8", buffering=1) as fout:
            fout.write(json.dumps(eval_result, ensure_ascii=False) + "\n")

    with open(filepath, "a", encoding="utf-8", buffering=1) as fout:
        fout.write(json.dumps(total_token_usage, ensure_ascii=False) + "\n")

    logger.info(f"评估结果: {eval_result}")
    logger.info(
        f"模型Token消耗统计:- 输入 (Prompt Tokens): {total_token_usage['prompt_tokens']} - 输出 (Completion Tokens): {total_token_usage['completion_tokens']} - 总计 (Total Tokens): {total_token_usage['total_tokens']}")
