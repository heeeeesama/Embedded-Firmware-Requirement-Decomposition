import json
import math
import re
from collections import Counter
from typing import List, Dict, Tuple
from rouge_score import rouge_scorer  # 需安装：pip install rouge-score


def normalize_answer(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def compute_f1(pred: str, goldens: List[str]) -> float:
    pred_norm = normalize_answer(pred)
    pred_tokens = pred_norm.split()
    max_f1 = 0.0

    for gold in goldens:
        gold_norm = normalize_answer(gold)
        gold_tokens = gold_norm.split()

        if not pred_tokens or not gold_tokens:
            f1 = 1.0 if (not pred_tokens and not gold_tokens) else 0.0
        else:
            common = Counter(pred_tokens) & Counter(gold_tokens)
            num_same = sum(common.values())
            if num_same == 0:
                f1 = 0.0
            else:
                precision = num_same / len(pred_tokens)
                recall = num_same / len(gold_tokens)
                f1 = 2 * precision * recall / (precision + recall)

        if f1 > max_f1:
            max_f1 = f1
    return max_f1


def compute_accuracy(pred: str, goldens: List[str]) -> float:
    pred_norm = normalize_answer(pred)
    for gold in goldens:
        gold_norm = normalize_answer(gold)
        if gold_norm in pred_norm:
            return 1.0
    return 0.0


def compute_rouge(pred: str, goldens: List[str]) -> Dict[str, float]:
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=False)
    max_rouge1 = 0.0
    max_rouge2 = 0.0
    max_rougel = 0.0

    for gold in goldens:
        scores = scorer.score(gold, pred)
        # 取f1值（precision和recall的调和平均）
        rouge1 = scores['rouge1'].fmeasure
        rouge2 = scores['rouge2'].fmeasure
        rougel = scores['rougeL'].fmeasure

        if rouge1 > max_rouge1:
            max_rouge1 = rouge1
        if rouge2 > max_rouge2:
            max_rouge2 = rouge2
        if rougel > max_rougel:
            max_rougel = rougel

    return {
        'rouge-1': max_rouge1,
        'rouge-2': max_rouge2,
        'rouge-l': max_rougel
    }


def evaluate_experiment(data) -> Tuple[Dict[str, float], List[Dict[str, float]]]:

    # with open(json_path, 'r', encoding='utf-8') as f:
    #     data = json.load(f)

    all_f1 = []
    all_acc = []
    all_rouge1 = []
    all_rouge2 = []
    all_rougel = []
    sample_scores = []

    for sample in data:
        pred = sample['pred']
        goldens = sample['golden_answers']
        sample_id = sample.get('id', 'unknown')

        f1 = compute_f1(pred, goldens)
        acc = compute_accuracy(pred, goldens)
        rouge = compute_rouge(pred, goldens)

        sample_scores.append({
            'id': sample_id,
            'f1': f1,
            'acc': acc,
            'rouge-1': rouge['rouge-1'],
            'rouge-2': rouge['rouge-2'],
            'rouge-l': rouge['rouge-l']
        })

        all_f1.append(f1)
        all_acc.append(acc)
        all_rouge1.append(rouge['rouge-1'])
        all_rouge2.append(rouge['rouge-2'])
        all_rougel.append(rouge['rouge-l'])

    overall = {
        'f1': sum(all_f1) / len(all_f1),
        'acc': sum(all_acc) / len(all_acc),
        'rouge-1': sum(all_rouge1) / len(all_rouge1),
        'rouge-2': sum(all_rouge2) / len(all_rouge2),
        'rouge-l': sum(all_rougel) / len(all_rougel)
    }

    return overall, sample_scores


def process_scores(scores_data):

    all_scores = []
    for item in scores_data:
        for algo, score in item["score"].items():
            all_scores.append(score)

    processed_scores = []
    for item in scores_data:
        for algo, score in item["score"].items():
            processed_scores.append(score)

    sorted_scores = sorted(processed_scores)
    n = len(sorted_scores)
    tenth_percentile_index = int(n * 0.1)
    ninetieth_percentile_index = int(n * 0.95)

    tenth_percentile = sorted_scores[tenth_percentile_index]
    ninetieth_percentile = sorted_scores[ninetieth_percentile_index]

    for item in scores_data:
        for algo in item["score"]:
            score = item["score"][algo]
            # 前10%赋予7分
            if score <= tenth_percentile:
                item["score"][algo] = 3
            # 后10%赋予3分
            elif score >= ninetieth_percentile:
               item["score"][algo] = 7
            # 其余保持不变

    epsilon = 1e-6
    for item in scores_data:
        for algo in item["score"]:
            score = item["score"][algo]
            sqrt_score = math.sqrt(score)
            log_score = math.log(sqrt_score + epsilon)
            item["score"][algo] = round(log_score, 4)

    return scores_data

# 示例用法
if __name__ == "__main__":
    # 替换为你的实验结果JSON路径
    experiment_json = "./all_results.json"

    methods = ["ircot", "iter-retgen", "SuRe", "base", "base_wo_retri", "deepnote", "mapping_base",
               "mapping_base_wo_retri", "mapping_miki"]

    with open(experiment_json, "r", encoding="utf-8") as f:
        all_results = json.load(f)

    for method in methods:
        data = []
        for index in range(len(all_results)):
            data.append({
                "id":str(index),
                "pred":all_results[index]["answers"][method],
                "golden_answers":all_results[index]["golden_answers"]
            })

        overall_metrics, sample_metrics = evaluate_experiment(data)

        print(method + " 总体评估指标：")
        for metric, score in overall_metrics.items():
            print(f"{metric}: {score:.4f}")

        with open(method + "_evaluation_details.json", "w", encoding="utf-8") as f:
            json.dump(sample_metrics, f, ensure_ascii=False, indent=2)

        print("\n详细结果已保存至 "+method+"_evaluation_details.json")


    score = process_scores(all_results)

    llm_judge = {"ircot": 0, "iter-retgen": 0, "SuRe": 0, "base": 0, "base_wo_retri": 0, "deepnote": 0,
                 "mapping_base": 0,
                 "mapping_base_wo_retri": 0, "mapping_miki": 0}
    for index in range(len(score)):
        for method in methods:
            llm_judge[method] = llm_judge[method] + score[index]["score"][method]
    for method in methods:
        llm_judge[method] = llm_judge[method] / len(score)

    print(llm_judge)



