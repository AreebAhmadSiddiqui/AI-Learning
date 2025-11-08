from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()

geminiModel=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')


docs = [
    Document(
        page_content="Virat Kohli is one of the greatest batsmen in the world. He is known for his aggression, consistency, and leadership. He has scored more than 7000 runs in IPL.",
        metadata={"player": "Virat Kohli", "ipl_team": "Royal Challengers Bengaluru"}
    ),
    Document(
        page_content="Rohit Sharma is famous for his elegant batting style and ability to score big hundreds. He is one of the most successful IPL captains with multiple titles.",
        metadata={"player": "Rohit Sharma", "ipl_team": "Mumbai Indians"}
    ),
    Document(
        page_content="MS Dhoni, also known as Captain Cool, is one of the most successful captains in cricket history. He has led Chennai Super Kings to multiple IPL trophies.",
        metadata={"player": "MS Dhoni", "ipl_team": "Chennai Super Kings"}
    ),
    Document(
        page_content="Jos Buttler is an explosive English opener known for his aggressive batting and ability to dominate powerplays. He won the Orange Cap in IPL 2022.",
        metadata={"player": "Jos Buttler", "ipl_team": "Rajasthan Royals"}
    ),
    Document(
        page_content="Shubman Gill is one of the most promising young Indian batsmen. He plays technically sound cricket and won the Orange Cap in IPL 2023.",
        metadata={"player": "Shubman Gill", "ipl_team": "Gujarat Titans"}
    ),
]


vector_store=Chroma(
    embedding_function=geminiModel,
    persist_directory='./code/rag/vector stores/my_chroma_db',
    collection_name='sample'
)


# Add documents

# result=vector_store.add_documents(docs)
# print(result)

# View documents

# print(vector_store.get(include=["embeddings", "metadatas", "documents"]))


# Similarity Search

print(vector_store.similarity_search(
    query='Who among these is the best cricketer',
    k=2
))


# Update documets

vector_store.update_document(document_id='c70b06c3-d44b-4263-a72f-4f77bcfc9b37',document=Document(
    page_content="MS Dhoni, also known as Captain Cool, is one of the most successful captains in cricket history. He has led Chennai Super Kings to multiple IPL trophies.",
        metadata={"player": "MS Dhoni", "ipl_team": "Chennai Super Kings"}
))


print(vector_store.get(ids=['c70b06c3-d44b-4263-a72f-4f77bcfc9b37']))


print(vector_store.delete(ids=['c70b06c3-d44b-4263-a72f-4f77bcfc9b37']))


print(vector_store.get(ids=['c70b06c3-d44b-4263-a72f-4f77bcfc9b37']))
