from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型对象
model = DashScopeEmbeddings()
# 调用模型
# 不用invoke stream
# embed_query,embed_documents = model.embed_documents(["你好"])
print(model.embed_query("你好")) #
print(model.embed_documents(["你好"]))