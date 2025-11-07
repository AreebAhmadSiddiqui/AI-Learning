from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
import time
loader= DirectoryLoader(
    path='./code/RAG/testForDirectoryLoader',
    glob='*pdf', # all files with pdf
    loader_cls=PyPDFLoader
)

# Load
start = time.time()

document=loader.load()
for doc in document:
    print(doc.metadata)

end = time.time()

print(f"Load Time Taken: {end-start}s")


# lazy_load
start = time.time()

document=loader.lazy_load()
for doc in document:
    print(doc.metadata)

end = time.time()

print(f"Lazy Load Time Taken: {end-start}s")
