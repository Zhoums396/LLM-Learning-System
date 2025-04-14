#!/bin/bash

# 确保Python环境已经安装了必要的依赖
echo "正在检查和安装必要的依赖..."
pip install flask requests

# 启动Flask应用
echo "启动智能学习助手应用..."
python app.py 