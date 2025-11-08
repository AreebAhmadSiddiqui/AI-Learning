# ✅ Imports
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()


# 🧾 Sample Docs
docs = [
    Document(page_content="Virat Kohli scored 973 runs in IPL 2016, leading RCB to the finals."),
    Document(page_content="He is one of the fittest players, known for his discipline and aggression."),
    Document(page_content="In 2023, Kohli scored two back-to-back centuries in IPL."),
]

# ⚙️ Vector Store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embedding=embeddings)
base_retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 🧠 Compressor (LLM-based summarizer)
llm = ChatOpenAI(model="gpt-3.5-turbo")
compressor = LLMChainExtractor.from_llm(llm)

# 🔄 Contextual Compression Retriever
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

# 🔍 Query
query = "How many runs did Virat Kohli score in IPL 2016?"
compressed_docs = compression_retriever.get_relevant_documents(query)

# 📄 Results
for i, doc in enumerate(compressed_docs, 1):
    print(f"\nResult {i}: {doc.page_content}")