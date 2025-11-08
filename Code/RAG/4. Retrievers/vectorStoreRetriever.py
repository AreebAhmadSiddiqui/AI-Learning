from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# 1. Create an embedding model
geminiModel=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')

# 2. Documents to store
docs = [
    Document(
        page_content="Virat Kohli is one of the greatest batsmen in the world. He is known for his aggression, consistency, and leadership. He has scored more than 7000 runs in IPL."
    ),
    Document(
        page_content="Rohit Sharma is famous for his elegant batting style and ability to score big hundreds. He is one of the most successful IPL captains with multiple titles."
    ),
    Document(
        page_content="MS Dhoni, also known as Captain Cool, is one of the most successful captains in cricket history. He has led Chennai Super Kings to multiple IPL trophies."
    ),
    Document(
        page_content="Jos Buttler is an explosive English opener known for his aggressive batting and ability to dominate powerplays. He won the Orange Cap in IPL 2022."
    ),
    Document(
        page_content="Shubman Gill is one of the most promising young Indian batsmen. He plays technically sound cricket and won the Orange Cap in IPL 2023."
    ),
]


# 3. Create ChromaDB

# In memory way
vector_store=Chroma.from_documents(
    documents=docs,
    embedding=geminiModel,
    collection_name='my_collection'
)

# # Hdd way
# vector_store=Chroma(
#     embedding_function=geminiModel,
#     persist_directory='./code/rag/vector stores/my_chroma_db',
#     collection_name='sample'
# )


# 4. Create Retriver
retriever=vector_store.as_retriever(search_kwargs={'k':1})

# 5. Query
query="Who is an elegant batsmen?"
results=retriever.invoke(query)

print(results)