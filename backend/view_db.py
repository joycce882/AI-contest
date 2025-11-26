from chromadb import PersistentClient

# 加载你的数据库
client = PersistentClient(path="./chroma_db")

# 查看所有 collections
collections = client.list_collections()
print("Collections:", collections)

# 如果你只有一个 collection，就取第一个
col = collections[0].name

collection = client.get_collection(name=col)

# 查看存了多少条数据
count = collection.count()
print(f"向量数量: {count}")

# 获取所有的数据
items = collection.get()
print("IDs:", items["ids"])
print("Metadatas:", items["metadatas"])
print("Documents:", items["documents"])
