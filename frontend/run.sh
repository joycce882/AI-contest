#!/bin/bash
# Linux/Mac 启动脚本 - 前端开发服务器

echo ""
echo "========================================"
echo " 银行业务问答系统 - 前端开发"
echo "========================================"
echo ""

# 检查 Node.js 是否安装
if ! command -v node &> /dev/null; then
    echo "[错误] Node.js 未安装"
    exit 1
fi

# 显示 Node 版本
echo "[信息] Node.js 版本："
node --version

# 检查依赖是否已安装
if [ ! -d "node_modules" ]; then
    echo "[信息] 安装依赖..."
    npm install
    if [ $? -ne 0 ]; then
        echo "[错误] npm 安装失败"
        exit 1
    fi
fi

# 启动开发服务器
echo "[信息] 启动前端开发服务器..."
echo "[提示] 访问地址：http://localhost:5173"
echo ""
npm run dev
