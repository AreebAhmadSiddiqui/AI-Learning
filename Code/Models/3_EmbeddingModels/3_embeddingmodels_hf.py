from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

result1 = embeddings.embed_query("Hello World")

# print(result1)



doc=[
    "Hello World 1",
    "Hello World 2",
    "Hello World 3",
]

result1 = embeddings.embed_documents(doc)

print(result1)