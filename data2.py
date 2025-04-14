import pandas as pd
import json
import re

def clean_question(text):
    if pd.isna(text):  # 处理缺失值
        return ""
    # 只保留汉字、字母、数字
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', str(text))
    # 去除多余空格
    text = re.sub(r'\s+', '', text)
    return text

# 清洗第二列
def clean_knowledge_point(text):
    if pd.isna(text):  # 处理缺失值
        return ""
    # 去除多余符号和空格
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', str(text))
    return text


# 读取test.json文件
with open('C:/Users/Administrator/Desktop/CJEval/data/CJEval_science/train/train_物理.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# with open('C:/Users/Administrator/Desktop/CJEval/data/CJEval_science/test_seen/test_物理.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

filename = data[0]['subject']

# print(filename)

# 提取需要的列
filtered_data = []
for item in data:
    filtered_data.append({
        'ques_content': item['ques_content'],
        'ques_difficulty': item['ques_difficulty']
    })

# 创建DataFrame
df = pd.DataFrame(filtered_data)

# 应用清洗函数
df['ques_content'] = df['ques_content'].apply(clean_question)  # 假设第一列列名为"题目内容"
df['ques_difficulty'] = df['ques_difficulty'].apply(clean_knowledge_point)  # 假设第二列列名为"题目难度"

# 去除空行（题目内容和知识点都为空的行）
df = df.dropna(subset=['ques_content', 'ques_difficulty'], how='all')

# 获取第一行subject的值作为文件名
file_name = filename + 'data_difficulty.csv'

# 保存为CSV文件
df.to_csv(file_name, index=False)
