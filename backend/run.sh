#!/bin/bash
# Linux/Mac 启动脚本 - 银行业务问答系统后端

echo ""
echo "========================================"
echo " 银行业务问答系统 - 后端服务启动"
echo "========================================"
echo ""

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "[错误] Python 3 未安装"
    exit 1
fi

# 检查虚拟环境（可选）
if [ -d "venv" ]; then
    echo "[信息] 激活虚拟环境..."
    source venv/bin/activate
fi

# 检查依赖
echo "[信息] 检查依赖..."
python3 -m pip list | grep fastapi > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "[信息] 安装依赖..."
    pip install fastapi uvicorn chromadb openai sentence-transformers python-dotenv pandas openpyxl
fi

# 启动服务
echo "[信息] 启动 FastAPI 服务..."
echo "[提示] API 地址：http://127.0.0.1:8000"
echo "[提示] API 文档：http://127.0.0.1:8000/docs"
echo ""
python3 main.py
