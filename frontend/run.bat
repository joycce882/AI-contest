@echo off
REM Windows 启动脚本 - 前端开发服务器

echo.
echo ========================================
echo  银行业务问答系统 - 前端开发
echo ========================================
echo.

REM 检查 Node.js 是否安装
node --version >nul 2>&1
if errorlevel 1 (
    echo [错误] Node.js 未安装或未添加到 PATH
    pause
    exit /b 1
)

REM 显示 Node 版本
echo [信息] Node.js 版本：
node --version

REM 检查依赖是否已安装
if not exist node_modules\ (
    echo [信息] 安装依赖...
    call npm install
    if errorlevel 1 (
        echo [错误] npm 安装失败
        pause
        exit /b 1
    )
)

REM 启动开发服务器
echo [信息] 启动前端开发服务器...
echo [提示] 访问地址：http://localhost:5173
echo.
npm run dev

pause
