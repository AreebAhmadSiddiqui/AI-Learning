from langchain_community.vectorstores import FAISS
from langchain.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI

# from 

load_dotenv()

docs = [
    Document(
        page_content="Virat Kohli is the highest run scorer in the history of IPL with more than 7000 runs.",
        metadata={"topic": "Batting Records", "year": "2023"}
    ),
    Document(
        page_content="Kohli’s best IPL season came in 2016 when he scored 973 runs with four centuries.",
        metadata={"topic": "Achievements", "year": "2016"}
    ),
    Document(
        page_content="Virat Kohli captained Royal Challengers Bengaluru for several years but has not won an IPL trophy.",
        metadata={"topic": "Captaincy", "year": "2021"}
    ),
    Document(
        page_content="Under Kohli’s leadership, RCB reached the IPL final in 2016 but lost to Sunrisers Hyderabad.",
        metadata={"topic": "Team Performance", "year": "2016"}
    ),
    Document(
        page_content="Kohli is known for his aggressive and passionate on-field behavior, often motivating his teammates.",
        metadata={"topic": "Personality", "year": "2020"}
    ),
    Document(
        page_content="In IPL 2023, Virat Kohli scored two back-to-back centuries, showing his consistency and hunger for runs.",
        metadata={"topic": "Recent Form", "year": "2023"}
    ),
    Document(
        page_content="Many analysts believe that Kohli’s captaincy helped groom young players like Siraj and Padikkal.",
        metadata={"topic": "Mentorship", "year": "2020"}
    ),
    Document(
        page_content="Despite consistent performances, Kohli faced criticism for not being able to secure an IPL title for RCB.",
        metadata={"topic": "Criticism", "year": "2019"}
    ),
    Document(
        page_content="Fans admire Kohli’s fitness and discipline, which have set new standards in the IPL.",
        metadata={"topic": "Fitness", "year": "2021"}
    ),
    Document(
        page_content="After stepping down as captain, Kohli continued to perform strongly as a batsman for RCB.",
        metadata={"topic": "Post-Captaincy", "year": "2022"}
    ),
]


# Step 1️⃣: Create embeddings
embeddings = GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')

# Step 2️⃣: Create vector store
vector_store = FAISS.from_documents(docs, embedding=embeddings)

# Step 3️⃣: Create base retriever
base_retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# Step 4️⃣: Initialize MultiQueryRetriever
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
multi_retriever = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=llm)

# Step 5️⃣: Test query
query = "Virat Kohli IPL performance"
results = multi_retriever.get_relevant_documents(query)

# Step 6️⃣: Display results
for i, doc in enumerate(results, 1):
    print(f"\nResult {i} ({doc.metadata['topic']} - {doc.metadata['year']}):")
    print(doc.page_content)