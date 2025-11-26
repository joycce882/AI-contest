from chromadb import PersistentClient
from typing import List
from openai import OpenAI
from sentence_transformers import SentenceTransformer


# =============== 1. 初始化 DeepSeek 客户端 ===============
# ⚠ 注意：不要把 key 写死在代码中！放环境变量里。
ai_client = OpenAI(
    api_key="sk-77b8fe40d425464e99b7a7040e639686",   # 直接写入测试
    base_url="https://api.deepseek.com"
)

# =============== 2. 初始化 bge-small-zh（512维）模型 ===============
embed_model = SentenceTransformer("BAAI/bge-small-zh")

# =============== 2. 加载 Chroma 数据库 ===============
client = PersistentClient(path="chroma_db")
try:
    collection = client.get_collection("excel_knowledge")
except Exception as e:
    print(f"❌ 错误：Collection 不存在: {e}")
    print("请先运行 build_index.py 来构建知识库")
    exit(1)


# =============== 3. 检索函数（生成 512 维 embedding） ===============
def retrieve_docs(query: str, top_k: int = 3):
    # 生成 512维 embedding（与数据库一致）
    emb = embed_model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[emb],
        n_results=top_k
    )
    return results["documents"][0]


# =============== 4. LLM 回答函数 ===============
def llm_answer(question: str, context: str) -> str:
    prompt = f"""你是一名银行业务智能助手，请严格根据知识库内容回答用户问题。

知识库内容：
{context}

用户问题：
{question}

请只基于知识库内容作答，不要编造不存在的信息。
"""

    resp = ai_client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )

    return resp.choices[0].message.content


# =============== 5. 主程序循环（异常则退出） ===============
if __name__ == "__main__":
    print("=== 智能业务助手测试（本地 RAG）===")
    print("输入 exit 或 quit 可退出程序\n")

    while True:
        q = input("\n请输入你的问题：").strip()

        if q.lower() in ["exit", "quit"]:
            print("程序已退出。")
            break

        # ---------- 检索知识库 ----------
        try:
            docs = retrieve_docs(q)
        except Exception as e:
            print("\n【检索失败】:", e)
            print("程序已退出。")
            break  # ❗检索失败直接退出

        print("\n【检索到的知识库片段】")
        for i, d in enumerate(docs):
            print(f"\n--- 片段 {i + 1} ---\n{d}")

        context = "\n\n".join(docs)

        # ---------- 调用 LLM ----------
        try:
            answer = llm_answer(q, context)
        except Exception as e:
            print("\n【LLM 调用失败】:", e)
            print("程序已退出。")
            break  # ❗LLM 出错也直接退出

        print("\n【AI 回答】")
        print(answer)
