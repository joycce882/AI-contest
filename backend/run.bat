@echo off
REM Windows 启动脚本 - 银行业务问答系统后端

echo.
echo ========================================
echo  银行业务问答系统 - 后端服务启动
echo ========================================
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] Python 未安装或未添加到 PATH
    pause
    exit /b 1
)

REM 检查虚拟环境（可选）
if exist venv\ (
    echo [信息] 激活虚拟环境...
    call venv\Scripts\activate.bat
)

REM 检查依赖
echo [信息] 检查依赖...
pip list | find "fastapi" >nul 2>&1
if errorlevel 1 (
    echo [信息] 安装依赖...
    pip install fastapi uvicorn chromadb openai sentence-transformers python-dotenv pandas openpyxl
)

REM 启动服务
echo [信息] 启动 FastAPI 服务...
echo [提示] API 地址：http://127.0.0.1:8000
echo [提示] API 文档：http://127.0.0.1:8000/docs
echo.
python main.py

pause
