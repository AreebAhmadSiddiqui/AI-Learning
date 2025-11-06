from langchain_community.document_loaders import CSVLoader

loader=CSVLoader('./code/rag/names.csv')

documentObj=loader.lazy_load()

for doc in documentObj:
    print(doc.page_content)