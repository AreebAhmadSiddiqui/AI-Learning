from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings


load_dotenv()
# 🧾 Create 5 diverse documents about Virat Kohli
docs = [
    Document(
        page_content=(
            "Virat Kohli has scored over 7000 runs in the Indian Premier League, "
            "making him the highest run scorer in IPL history."
        ),
        metadata={"topic": "Batting Records", "team": "Royal Challengers Bengaluru"}
    ),
    Document(
        page_content=(
            "Virat Kohli captained the Royal Challengers Bengaluru for nearly a decade, "
            "leading them to the finals in 2016 where they finished as runners-up."
        ),
        metadata={"topic": "Captaincy", "team": "Royal Challengers Bengaluru"}
    ),
    Document(
        page_content=(
            "In the 2016 IPL season, Virat Kohli scored a record-breaking 973 runs, "
            "including four centuries, the most by any player in a single season."
        ),
        metadata={"topic": "Achievements", "team": "Royal Challengers Bengaluru"}
    ),
    Document(
        page_content=(
            "Virat Kohli is known for his aggressive leadership style and consistency, "
            "setting high standards for fitness and discipline in the IPL."
        ),
        metadata={"topic": "Personality & Leadership", "team": "Royal Challengers Bengaluru"}
    ),
    Document(
        page_content=(
            "Under Kohli’s leadership, RCB developed young Indian talents like Mohammed Siraj "
            "and Devdutt Padikkal, who became key players for the team."
        ),
        metadata={"topic": "Team Development", "team": "Royal Challengers Bengaluru"}
    ),
]


# 1. Create an embedding model
geminiModel=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')

# 2. store
vector_store=FAISS.from_documents(
    documents=docs,
    embedding=geminiModel
)

# Enable MMR
retriever=vector_store.as_retriever(
    search_type='mmr',
    search_kwargs={'k':3,'lambda_mult':1}
)

query='Virat Kohli IPL career'
print(retriever.invoke(query))


