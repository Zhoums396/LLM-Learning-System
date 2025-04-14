# 智能学习助手

基于大模型的学科问题分析与个性化学习推荐系统。

## 功能特点

- 自动分析学科题目，识别学科类型
- 提取关键知识点
- 评估题目难度级别
- 提供清晰直观的可视化结果

## 安装与运行

### 环境要求

- Python 3.7+
- Node.js 14+ (仅用于npm命令)

### 安装依赖

```bash
pip install flask requests
```

### 运行应用

方法1：直接使用Python

```bash
python app.py
```

方法2：使用npm

```bash
npm run dev
```

## 使用方法

1. 启动应用后，访问 http://127.0.0.1:5000
2. 在文本框中输入学科题目
3. 点击"开始分析"按钮
4. 查看分析结果

## API配置

在`app.py`文件中配置您的API密钥：

```python
API_KEY = "your-api-key"
BASE_URL = "your-api-base-url"
``` 