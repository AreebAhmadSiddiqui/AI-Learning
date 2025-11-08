# 🧠 Vector Stores (In Easy Hinglish)

## 📘 Pehle basic samajh lo: Vector kya hota hai?

Machine Learning aur AI mein, **vector** ka matlab hota hai —  
ek **numbers ki list (array)** jo kisi cheez (jaise text, image, ya audio) ka **mathematical representation** hoti hai.

**Example:**  
"Apple" ko ek vector ke form mein store karte hain jaise:  
`[0.21, -0.53, 0.88, ...]`  

Yeh numbers "apple" ke **meaning** ko represent karte hain —  
toh agar tum "mango" ka vector dekho, wo bhi similar hoga,  
kyunki dono fruits hain 🍎🥭  

---

## 📦 Ab samjho: Vector Store kya hai?

**Vector Store** ek **database** hota hai jisme hum ye saare **vectors (embeddings)** store karte hain.  
Simple words mein —

> Ye ek jagah hai jahan tum apne “text ke mathematical versions” save karte ho taaki baad mein unhe meaning ke basis pe search kar sako.

Normal database (like SQL, MongoDB) **exact match search** karta hai —  
par **Vector Store** karta hai **semantic search** (meaning-based search).

---

## 🔍 Example samjho

Tumhare paas kuch documents hain:  

1. “AI is changing the world.”  
2. “Cricket is the most popular sport in India.”  
3. “Machine learning helps in automation.”

Agar tum query likho:  
> “What is artificial intelligence doing?”

Toh normal search system exact words dekhega (AI, doing etc.).  
Par **Vector Store** meaning samjhta hai —  
usko pata hai “Artificial Intelligence” = “AI”,  
toh wo **Document 1** ko top result mein la dega.  

---

## 🧩 Vector Store ka kaam kaise hota hai?

1. **Embedding banao**  
   - Har text ko ek model (like OpenAI Embeddings, HuggingFace, etc.) se **vector mein convert** karo.  
   - Example: `"AI is changing the world"` → `[0.23, -0.12, 0.77, ...]`

2. **Store karo**  
   - Ye vectors **Vector Store** mein save karte hain (along with original text). 
   - Can be stores in RAM ( Wipes as you close the app) as well as hard drive or other db ( vectors persist) 

3. **Query karo**  
   - Jab user koi query karta hai, us query ko bhi vector mein convert karte hain.  

4. **Similarity Search**  
   - Indexing ka use karta hai
   - Store ke vectors se compare karte hain —  
     jiska **cosine similarity** sabse zyada hota hai (i.e. meaning closest hota hai), wo result return karte hain.

---

## ⚙️ Common Vector Stores

| Vector Store | Description |
|---------------|-------------|
| **FAISS** (by Facebook) | Fast, local & free; used for small to medium projects. |
| **Pinecone** | Cloud-based, scalable, easy to use API. |
| **Weaviate** | Open-source, supports hybrid search (keyword + semantic). |
| **Chroma** | Simple & popular for LLM apps (used with LangChain). |
| **Milvus** | High performance, open-source, enterprise-grade. |

---

## 🧱 Use Cases (Kaha kaam aata hai?)

1. **RAG (Retrieval-Augmented Generation)**  
   → LLM ko context dene ke liye relevant documents retrieve karne mein.  
2. **Semantic Search**  
   → “Meaning-based” search engines banane mein.  
3. **Recommendation Systems**  
   → Similar products / movies / articles suggest karne mein.  
4. **Chat with your Docs**  
   → Apne PDF, notes ya website data se chat karne wale AI apps mein.

---


## Movie Recommendation System 

- Tumne keuwords se agar movies recommend kari to ho sakta hai ki movies mein ko bhi similarity na ho bas actors, directors ko dekh ke recommend ho jae
- To best hoga ki plot ko compare karo
- To do this we create embeddings of the plot for each movie and then recommend the movie whose plot is similar


# Challenges

- Generating embeddings vector
- Storage is different for these embeddings ( SQL, NoSQL can't be used because they dont persist semantic meanings)
- Semantic search intellisense


## How does it search so fast in a vector store

- This is one of the way
- Normal mein to ek query vector ko 10 lakh vectors se compare karna padega
- Indexing + clustering is used 
- Manlo 10 lakh vectors hai to clustering techniques ka use karke 10 clusters form kar liye ( example)
- Ab har 10 clusters ka centroid nikal lo
- Ab sirf in 10 clusters mein se compare karo
- Jis cluster ka similar ae bas usi cluster ko use karo

### 🚀 Step 2: Smart Techniques (Speed ke liye Tricks)

#### 1. Approximate Nearest Neighbor (ANN) Search

- Instead of checking every single vector,
wo approximate (nearby) vectors ko hi check karte hain.
- Matlab — 100% accurate nahi,
but 99% accurate aur 100x faster ⚡

#### Example Libraries:

- FAISS (Facebook AI Similarity Search)
- Annoy (Spotify)
- HNSW (Hierarchical Navigable Small World Graph)

### 2. Vector Indexing (Fast lookup system)

- Vector store ek index banata hai —
jisse vectors ko mathematically cluster karke rakhte hain.
- So jab query aati hai,
wo directly usi cluster mein jaata hai jahan relevant vectors hone ke chances zyada hain.
- Socho jaise ek library mein tum “AI” wali shelf pe seedha chale jaate ho
instead of checking har shelf 😄

## Vector Store vs Vector Databases

- Vector store's major functions 
   - Storage
   - Retrieval ( similarity search)

- Vector db is vector store plus additional db features
   - distributed systems
   - durability
   - authentication etc


## Chroma DB 

- Hai vector db lekin light weight
- To it is in between store and db

In memory way

### In memory way
vector_store=Chroma.from_documents(
    documents=docs,
    embedding=geminiModel,
    collection_name='my_collection'
)

### In HDD way
vector_store=Chroma(
    embedding_function=geminiModel,
    persist_directory='./code/rag/vector stores/my_chroma_db',
    collection_name='sample'
)
