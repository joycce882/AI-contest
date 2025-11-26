# FastAPI 主程序 - 银行业务智能问答系统
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chromadb import PersistentClient
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# 加载环境变量
load_dotenv()

print("🚀 启动银行业务问答系统...")

# 初始化 FastAPI 应用
app = FastAPI(title="银行业务问答系统", version="1.0.0")

# 配置 CORS（允许前端跨域请求）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化 DeepSeek 客户端
api_key = os.getenv("DEEPSEEK_API_KEY")
ai_client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

# 初始化向量模型
embed_model = SentenceTransformer("BAAI/bge-small-zh")

# 加载 Chroma 数据库
try:
    db_path = r"f:\work_match_vs\backend\chroma_db"
    client = PersistentClient(path=db_path)
    collection = client.get_collection("excel_knowledge")
    print("✅ 向量数据库加载成功")
except Exception as e:
    print(f"❌ 向量数据库加载失败: {e}")
    print("请先运行 build_index.py 构建知识库")
    raise

# =============== 定义请求/响应模型 ===============
class Query(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    context: List[str]

class HealthResponse(BaseModel):
    status: str
    message: str


# =============== RAG 检索逻辑 ===============
def retrieve_docs(query: str, top_k: int = 3) -> List[str]:
    """从向量数据库检索相关文档"""
    try:
        # 使用 embed_model 生成 embedding（与 outputtest.py 相同方法）
        emb = embed_model.encode([query]).tolist()[0]
        
        results = collection.query(
            query_embeddings=[emb],
            n_results=top_k
        )
        docs = results["documents"][0] if results["documents"] else []
        return docs
    except Exception as e:
        print(f"❌ 检索失败: {e}")
        raise HTTPException(status_code=500, detail=f"知识库检索失败: {str(e)}")


# =============== 大模型回答 ===============
def llm_answer(question: str, context: str) -> str:
    """使用 DeepSeek LLM 生成回答"""
    try:
        prompt = f"""你是一名银行业务智能助手，请根据给定的知识库内容回答用户问题。

知识库内容：
{context}

用户问题：
{question}

请根据知识库内容准确回答，不要编造不存在的信息。如果知识库中没有相关信息，请告诉用户。
"""

        resp = ai_client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        
        return resp.choices[0].message.content
    except Exception as e:
        print(f"❌ LLM 调用失败: {e}")
        raise HTTPException(status_code=500, detail=f"AI 服务错误: {str(e)}")


# =============== API 端点 ===============

@app.get("/health", response_model=HealthResponse)
def health_check():
    """健康检查端点"""
    return HealthResponse(
        status="ok",
        message="后端服务正常运行"
    )


@app.post("/ask", response_model=AnswerResponse)
def ask_question(query: Query):
    """问答端点 - 接收问题并返回 AI 回答"""
    try:
        # 检索知识库
        docs = retrieve_docs(query.question, top_k=3)
        if not docs:
            raise HTTPException(status_code=404, detail="知识库中未找到相关信息")
        
        # 拼接上下文
        context = "\n\n".join(docs)
        
        # 调用 LLM
        answer = llm_answer(query.question, context)
        
        return AnswerResponse(answer=answer, context=docs)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/anti-fraud-tags")
def get_anti_fraud_tags():
    """获取防诈知识标签"""
    return {
        "tags": [
            {"id": 1, "name": "电信诈骗", "icon": "warning"},
            {"id": 2, "name": "冒充身份", "icon": "user-secret"},
            {"id": 3, "name": "虚假投资", "icon": "chart-line"},
            {"id": 4, "name": "钓鱼网站", "icon": "link"}
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=False
    )