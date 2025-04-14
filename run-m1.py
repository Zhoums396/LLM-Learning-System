import os
from transformers import BertTokenizer, BartForConditionalGeneration

# 加载分词器
tokenizer = BertTokenizer.from_pretrained("fnlp/bart-base-chinese")

# 获取最新的 checkpoint 目录
results_dir = "C:/Users/Administrator/Desktop/CJEval/results-m1"
latest_checkpoint = max(
    [os.path.join(results_dir, d) for d in os.listdir(results_dir) if d.startswith("checkpoint")],
    key=os.path.getmtime
)

# 加载最新的 checkpoint
model = BartForConditionalGeneration.from_pretrained(latest_checkpoint)
print(f"成功加载模型：{latest_checkpoint}")

model.eval()

def predict(text):
    # 对输入进行编码
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    
    # 只保留 model 需要的参数
    inputs = {k: v for k, v in inputs.items() if k in ["input_ids", "attention_mask"]}
    
    # 生成预测
    output_ids = model.generate(**inputs, max_length=128, num_beams=5)
    
    # 解码预测结果（保持逗号）
    predicted_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # **用 ", " 作为知识点分隔符，并去掉空格**
    predicted_labels = [label.strip().replace(" ", "") for label in predicted_text.split(",") if label.strip()]
    
    return predicted_labels  # 返回一个知识点列表

# 测试预测
# test_text = "题目内容在国际单位制中用来表示时间的基本单位是选项A小时B毫秒C秒D分钟"
# prediction = predict(test_text)
# print("预测的知识点类型:", prediction)

import pandas as pd
from sklearn.metrics import f1_score, jaccard_score
from ast import literal_eval  # 解析存储为字符串的列表

test_df = pd.read_csv("Test-m.csv")

# 进行批量预测
test_df["predicted_ques_knowledges"] = test_df["ques_content"].apply(predict)

# 解析真实标签
test_df["ques_knowledges"] = test_df["ques_knowledges"].apply(lambda x: x.split(",") if isinstance(x, str) else [])

# 计算 Jaccard 相似度
def jaccard_similarity(list1, list2):
    set1, set2 = set(list1), set(list2)
    return len(set1 & set2) / len(set1 | set2) if len(set1 | set2) > 0 else 0

test_df["jaccard"] = test_df.apply(lambda row: jaccard_similarity(row["ques_knowledges"], row["predicted_ques_knowledges"]), axis=1)

# 计算平均 Jaccard 相似度
mean_jaccard = test_df["jaccard"].mean()
print(f"模型在测试集上的平均 Jaccard 相似度: {mean_jaccard:.4f}")

# 计算 Micro-F1 分数
y_true = test_df["ques_knowledges"]
y_pred = test_df["predicted_ques_knowledges"]

# 需要把列表转换为 one-hot 形式
from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
y_true_bin = mlb.fit_transform(y_true)  # 真实标签
y_pred_bin = mlb.transform(y_pred)  # 预测标签（必须使用同样的 `mlb`）

f1 = f1_score(y_true_bin, y_pred_bin, average="micro")
print(f"模型在测试集上的 Micro-F1 分数: {f1:.4f}")

# 保存预测结果
test_df.to_csv("predicted_test_m1.csv", index=False)

