import json
import os
import time
import numpy as np
import requests
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from neo4j import GraphDatabase

DEVICE_JSON_PATH = "./devices.json"  # 设备知识库文件路径
QUESTION_FILE_PATH = "../data/eval/bmcqa/test.json"  # 存储问题JSON的目录（需提前创建）
OUTPUT_RESULT_FILE = "match_results.json"  # 匹配结果保存路径
MODEL_PATH = "/model/bge-m3"

NEO4J_URL = "bolt://localhost:7687"
NEO4J_USERNAME = "******"
NEO4J_PASSWORD = "***********"

# 全局变量初始化
model = None  # 文本嵌入模型
device_data = []  # 存储设备原始数据 [{"name": "...", "description": "..."}]
description_embeddings = None  # 存储所有description的向量嵌入
entity_search_prompt = None
with open('./entity_search_prompt.txt', 'r', encoding='utf-8') as f:
    entity_search_prompt = f.read()


def load_device_knowledge_base(json_path="devices.json"):
    """
    加载设备知识库（device.json）
    :param json_path: 设备JSON文件路径
    :return: 设备数据列表
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("devices.json error")
    print(f"成功加载设备知识库，共包含 {len(data)} 个设备")
    return data


def init_embedding_model(model_path="all-MiniLM-L6-v2"):
    """
    初始化文本嵌入模型（轻量、高效，支持中英双语语义匹配）
    :param model_path: 模型名称
    :return: 初始化后的模型
    """
    try:
        model = SentenceTransformer(model_path, device='cpu')
        print("模型加载完成")
        return model
    except Exception as e:
        print(f"模型加载失败：{str(e)}")
        exit(1)


def build_device_embedding():
    """
    为设备知识库的description生成语义向量
    """
    global description_embeddings
    # 提取所有设备的description文本
    descriptions = [item["description"] for item in device_data]
    # 生成向量嵌入
    description_embeddings = model.encode(descriptions, convert_to_numpy=True)
    print(f"设备知识库向量构建完成，共生成 {len(description_embeddings)} 个向量")


def extract_entity_from_question(question):
    """
    调用Ollama的qwen3-8b提取问题中的核心实体
    :param question: 原始问题文本
    :return: 提取的实体（失败则返回原始question）
    """

    prompt = entity_search_prompt.replace("{question}", question)
    # 调用Ollama API

    data = {
        "model": "qwen3:8b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "top_p": 0.9,
            "num_predict": 2000
        }
    }

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
            timeout=120
        )
        response.raise_for_status()
        response_data = response.json()
        entity = response_data.get("response", "").strip()
        # 可能匹配不到实体
        if len(entity) > 2:
            print(f"原始问题：{question}")
            print(f"提取实体：{entity}\n")
            return entity
        else:
            # 问题嵌入
            question_embedding = model.encode([question], convert_to_numpy=True)
            # 余弦相似度
            similarities = cosine_similarity(question_embedding, description_embeddings)[0]
            # top 1 entity
            top_idx = np.argsort(similarities)[::-1][0]

            entity_name = device_data[top_idx]["name"]
            return f"[\"{entity_name}\"]"
    except Exception as e:
        print(f"提取实体失败：{str(e)}")
        return question


def entity_search(file_path):
    """
    读取question
    :param file_path: 存储问题JSON的目录路径
    :return entity_list: 问题列表，格式：[{"question": 问题内容, "entity":问题对应的实体, "index": 问题索引}]
    """
    entities_list = []

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for idx, item in enumerate(data):
        if "question" in item and item["question"].strip():
            entity = extract_entity_from_question(item["question"].strip())
            parsed_entity = json.loads(entity)
            entities_list.append({
                "question": item["question"].strip(),
                "entity": parsed_entity,
                "index": idx
            })
        else:
            continue

    with open("./entity_search_results.json", "w", encoding="utf-8") as f:
        json.dump(entities_list, f, ensure_ascii=False, indent=4)

    return entities_list


def find_paths_between_entities(start_name, end_name, max_path_length=10):
    """
    查找Neo4j数据库中从name为start_name的节点到name为end_name的节点的所有路径

    参数:
    uri (str): Neo4j数据库的连接URI
    username (str): 数据库用户名
    password (str): 数据库密码
    start_name (str): 起始节点的name属性值
    end_name (str): 目标节点的name属性值
    max_path_length (int): 最大路径长度，防止无限循环或性能问题

    返回:
    list: 包含所有路径的列表，每条路径是一个字典，包含节点列表和关系列表
    """
    paths = []

    # 连接到Neo4j数据库
    with GraphDatabase.driver(NEO4J_URL, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)) as driver:
        # 执行Cypher查询
        query = f"""
            MATCH path = (start {{name: $start_name}})-[*1..{max_path_length}]->(end {{name: $end_name}})
            RETURN nodes(path) AS nodes, relationships(path) AS rels
            """

        with driver.session() as session:
            result = session.run(
                query,
                start_name=start_name,
                end_name=end_name
            )

            # 处理查询结果
            for record in result:
                # 提取节点和关系
                nodes = record["nodes"]
                rels = record["rels"]

                # 转换为字典表示
                path_info = {
                    "nodes": [{"id": node.id, "properties": dict(node)} for node in nodes],
                    "relationships": [{"id": rel.id, "type": rel.type, "properties": dict(rel)} for rel in rels],
                    "length": len(rels)
                }

                paths.append(path_info)

    return paths


def convert_to_natural_language(query_result):
    descriptions = []

    for path in query_result:
        nodes = path['nodes']
        relationships = path['relationships']

        # 提取BMC节点信息
        bmc_node = next((node for node in nodes if 'manufacturer' in node['properties']), None)
        if not bmc_node:
            continue

        bmc_props = bmc_node['properties']
        bmc_desc = (f"BMC(名称: {bmc_props['name']}, 芯片: {bmc_props['chip']}, "
                    f"制造商: {bmc_props['manufacturer']}, 描述: {bmc_props['description']})")

        # 提取并描述链路关系
        path_descriptions = []
        current_device = bmc_desc

        for i, rel in enumerate(relationships):
            rel_props = rel['properties']
            next_node = nodes[i + 1]['properties']

            # 构建设备描述
            device_desc = f"{next_node['name']}(芯片: {next_node['chip']}"
            if 'function' in next_node:
                device_desc += f", 功能: {next_node['function']}"
            device_desc += f", 描述: {next_node['description']})"

            # 根据关系类型构建描述
            if rel['type'] == 'DIRECT_CONTROL':
                rel_desc = (f"通过{rel_props['bus_name']}总线({rel_props['protocol']}协议)直接控制, "
                            f"访问地址: {rel_props['access_address']}")
                path_descriptions.append(f"{current_device} {rel_desc} 连接到 {device_desc}")

            elif rel['type'] == 'SWITCH_ROUTE':
                if rel_props['switch_type'] == 'I2C Switch':
                    rel_desc = (f"通过{rel_props['switch_type']}(地址: {rel_props['switch_bus_address']})"
                                f"的通道{rel_props['channel_address']}路由({rel_props['protocol']}协议)")
                path_descriptions.append(f"{current_device} {rel_desc} 连接到 {device_desc}")

            elif rel['type'] == 'REGISTER_PROXY':
                ref_doc = rel_props.get('ref_doc', '无参考文档')
                rel_desc = f"通过寄存器代理控制(参考文档: {ref_doc})"
                path_descriptions.append(f"{current_device} {rel_desc} 连接到 {device_desc}")

            current_device = next_node['name']

        descriptions.append("\n".join(path_descriptions))

    return "\n\n".join(descriptions)


def hardware_topology_retrieval(entities):
    hardware_topology = []

    for item in entities:
        hardware_topology_description = ""
        for entity in item["entity"]:
            # 寻找硬件连接路径
            hardware_path = find_paths_between_entities("bmc", entity)

            # 转换为自然语言描述
            hardware_topology_description += convert_to_natural_language(hardware_path)

        hardware_topology.append({
                "question": item["question"].strip(),
                "entity": item["entity"],
                "index": item["index"],
                "hardware_topology": hardware_topology_description
        })

    with open("./hardware_topology.json", "w", encoding="utf-8") as f:
        json.dump(hardware_topology, f, ensure_ascii=False, indent=4)

    return hardware_topology

if __name__ == "__main__":
    # 加载设备知识库
    device_data = load_device_knowledge_base(DEVICE_JSON_PATH)
    
    # 初始化嵌入模型
    model = init_embedding_model(MODEL_PATH)
    
    # 设备知识库的嵌入
    build_device_embedding()
    
    # 实体识别
    entities_list = entity_search(QUESTION_FILE_PATH)
    
    # with open("./entity_search_results.json", "r", encoding="utf-8") as f:
    #     entities_list = json.load(f)
    
    hardware_topology_retrieval(entities_list)

    # 合并数据集和硬件拓扑检索结果
    dataset = []
    hardware_topology = []
    dataset_with_hardware_topology = []
    with open("./benchmark.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)
    with open("./hardware_topology.json", "r", encoding="utf-8") as f:
        hardware_topology = json.load(f)

    for idx, requirement in enumerate(dataset):
        dataset_with_hardware_topology.append({
            "question": requirement["question"],
            "hardware_topology": hardware_topology[idx]["hardware_topology"],
            "qa_pairs": requirement["qa_pairs"]
        })

    with open("./dataset_with_hardware_topology.json", "w", encoding="utf-8") as f:
        json.dump(dataset_with_hardware_topology, f, ensure_ascii=False, indent=4)