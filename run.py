import os
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from transformers import BertTokenizer, BartForConditionalGeneration

# 加载分词器
tokenizer = BertTokenizer.from_pretrained("fnlp/bart-base-chinese")

# 获取最新的 checkpoint 目录
results_dir = "C:/Users/Administrator/Desktop/CJEval/results2"
latest_checkpoint = max(
    [os.path.join(results_dir, d) for d in os.listdir(results_dir) if d.startswith("checkpoint")],
    key=os.path.getmtime
)

# 加载最新的 checkpoint
model = BartForConditionalGeneration.from_pretrained(latest_checkpoint)
print(f"成功加载模型：{latest_checkpoint}")

model.eval()

def predict(text):
    # 对输入进行编码（移除 token_type_ids）
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    
    # 只保留 model 需要的参数
    inputs = {k: v for k, v in inputs.items() if k in ["input_ids", "attention_mask"]}
    
    # 生成预测
    output_ids = model.generate(**inputs, max_length=128, num_beams=5)
    
    # 解码预测结果并删除空格
    predicted_text = tokenizer.decode(output_ids[0], skip_special_tokens=True).replace(" ", "")
    return predicted_text

# 读取测试数据
test_df = pd.read_csv("Test.csv")

# 进行批量预测
test_df["predicted_ques_knowledges"] = test_df["ques_content"].apply(predict)

# 计算准确率
y_true = test_df["ques_knowledges"].astype(str)  # 真实标签
y_pred = test_df["predicted_ques_knowledges"].astype(str)  # 预测标签

accuracy = accuracy_score(y_true, y_pred)  # 计算准确率
f1 = f1_score(y_true, y_pred, average="weighted")  # 计算加权 F1-score

print(f"模型在测试集上的准确率: {accuracy:.4f}")
print(f"模型在测试集上的 F1-score: {f1:.4f}")

# 保存预测结果
test_df.to_csv("predicted_test3.csv", index=False)