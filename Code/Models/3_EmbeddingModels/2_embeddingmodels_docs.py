from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')

doc=[
    "Hello World 1",
    "Hello World 2",
    "Hello World 3",
]
result = embeddings.embed_documents(doc)

print(result)