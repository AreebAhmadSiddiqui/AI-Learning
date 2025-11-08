from langchain_community.retrievers import WikipediaRetriever

retriever=WikipediaRetriever(top_k_results=2,lang='en')

query='Who is Virat Kohli'
docs=retriever.invoke(query)

# print(docs)

for doc in docs:
    print(doc.page_content)