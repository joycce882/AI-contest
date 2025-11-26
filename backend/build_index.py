# 向量库
import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb

# 1. read excel
df = pd.read_excel("./data.xlsx")

def row_to_text(row):
    return f"""
业务名称：{row['业务名称']}
业务别名：{row['业务别名']}
推荐渠道：{row['推荐渠道']}
其他渠道：{row['其他渠道']}
必须证件：{row['必须证件']}
相关辅助材料：{row['相关辅助材料']}
办理流程说明：{row['办理流程说明']}
是否必须为本人：{row['是否必须为本人']}
""".strip()

docs = df.apply(row_to_text, axis=1).tolist()
ids = df.index.astype(str).tolist()

# embedding model
model = SentenceTransformer("BAAI/bge-small-zh")

embs = model.encode(docs, show_progress_bar=True)

# store
client = chromadb.PersistentClient(path="chroma_db")
coll = client.get_or_create_collection("excel_knowledge")

coll.add(
    documents=docs,
    embeddings=embs,
    ids=ids
)

print("知识库构建完成！")
