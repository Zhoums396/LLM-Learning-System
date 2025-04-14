import json
import os

# 定义文件路径
file_paths = ['C:/Users/Administrator/Desktop/CJEval/data/CJEval_science/train/train_地理1.json', 
              'C:/Users/Administrator/Desktop/CJEval/data/CJEval_science/train/train_化学1.json', 
              'C:/Users/Administrator/Desktop/CJEval/data/CJEval_science/train/train_生物1.json', 
              'C:/Users/Administrator/Desktop/CJEval/data/CJEval_science/train/train_物理.json']

# 遍历每个文件
for file_path in file_paths:
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"文件 {file_path} 不存在，跳过。")
        continue

    # 读取 JSON 文件
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 打印基本信息
    print(f"\n=== {file_path} 基本信息 ===")
    
    # 1. 查看数据类型
    print(f"数据类型: {type(data)}")

    # 2. 查看数据长度（题目数量）
    if isinstance(data, list):
        print(f"题目数量: {len(data)}")
    elif isinstance(data, dict):
        print(f"字典键数量: {len(data)}")
    else:
        print("数据格式未知，无法统计题目数量。")

    # 3. 查看第一道题目的结构（示例）
    if isinstance(data, list) and len(data) > 0:
        print("\n第一道题目示例:")
        print(json.dumps(data[0], indent=4, ensure_ascii=False))
    elif isinstance(data, dict) and len(data) > 0:
        first_key = list(data.keys())[0]
        print("\n第一道题目示例:")
        print(json.dumps(data[first_key], indent=4, ensure_ascii=False))
    else:
        print("无题目数据或数据格式不支持。")

    # 4. 查看题目字段（假设每道题目是一个字典）
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        print("\n题目字段:")
        print(list(data[0].keys()))
    elif isinstance(data, dict) and len(data) > 0 and isinstance(data[list(data.keys())[0]], dict):
        print("\n题目字段:")
        print(list(data[list(data.keys())[0]].keys()))
    else:
        print("无法提取题目字段信息。")

    # 5. 统计知识点数量（假设每道题目有一个知识点列表）
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict) and 'ques_knowledges' in data[0]:
        knowledge_points = set()
        for question in data:
            knowledge_points.update(question.get('ques_knowledges', []))
        print(f"\n知识点数量: {len(knowledge_points)}")
    else:
        print("无法统计知识点数量。")

    # 6. 统计难度分布（假设每道题目有一个难度字段）
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict) and 'ques_difficulty' in data[0]:
        difficulty_distribution = {}
        for question in data:
            difficulty = question.get('ques_difficulty', '未知')
            difficulty_distribution[difficulty] = difficulty_distribution.get(difficulty, 0) + 1
        print("\n难度分布:")
        for difficulty, count in difficulty_distribution.items():
            print(f"{difficulty}: {count} 题")
    else:
        print("无法统计难度分布。")

    print("\n" + "=" * 40 + "\n")








# import os
# import json

# # 定义文件路径
# base_path = 'CJEval_data\CJEval_data'

# # 定义学科列表
# subjects = ['初中地理', '初中化学', '初中生物', '初中物理', '初中信息技术']

# # 定义数据集类型
# data_types = ['train', 'val', 'test']

# # 遍历每个学科和数据集类型
# for subject in subjects:
#     for data_type in data_types:
#         file_path = os.path.join(base_path, data_type, f'{data_type}_{subject}.json')
        
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 data = json.load(file)
#                 # 这里可以对数据进行处理，比如统计数量
#                 print(f'{data_type}_{subject}.json contains {len(data)} entries.')
#         else:
#             print(f'File {file_path} does not exist.')




''' prompt模板
任务：根据题目内容，预测其所属的知识点类型和难度级别。
知识点类型包括：常见物体的长度, 时间的测量, 机械运动, 温度的概念...
难度级别包括：容易、较易、一般、较难、困难

示例1：
题目：跳远运动员在起跳前都会进行一段助跑这是为什么?
知识点类型：惯性的利用及危害防止，难度级别：简单。

示例2：
题目：当锤柄向下撞击硬物时为什么锤头会紧密地套在锤柄上?
知识点类型：惯性现象，难度级别：简单。

请预测以下题目的知识点类型和难度级别：
题目：在盆中装满水并向前移动当盆突然停止时为什么水会继续向前溅出?
知识点类型：，难度级别：。

sk-1j7mcf0lf559ekhltu36sciuot4jd94jhu51qp76j2skjikk

from openai import OpenAI

client = OpenAI(
  api_key="sk-1j7mcf0lf559ekhltu36sciuot4jd94jhu51qp76j2skjikk"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);

'''

