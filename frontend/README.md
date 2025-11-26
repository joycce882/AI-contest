# Vite 前端项目

## 环境变量配置

创建 `.env.local` 文件：

```
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## 安装依赖

```bash
npm install
# 或
pnpm install
# 或
yarn install
```

## 开发

```bash
npm run dev
```

访问 http://localhost:5173

## 构建

```bash
npm run build
```

## API 代理

Vite 配置了 `/api` 前缀的代理，所有 API 请求会自动转发到 `http://127.0.0.1:8000`。
