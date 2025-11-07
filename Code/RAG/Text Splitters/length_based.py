from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text="""
    In our hyper-connected world, boredom is treated as a failure of stimulation, an emptiness to be filled with digital noise. We instinctively reach for our phones, seeking refuge from the quiet moment. Yet, it is in this very space of perceived idleness that creativity often sparks. When the mind is unoccupied by external inputs, it turns inward. It wanders, connects disparate ideas, and daydreams. This mental wandering is not a waste of time; it is the subconscious workshop where problems are solved and new perspectives are born. By constantly avoiding boredom, we may be sacrificing our most profound creative potential. The richest ideas often emerge not from focused effort, but from the quiet, fertile ground of a mind allowed to be adrift. Embracing occasional boredom could be the key to unlocking a deeper, more imaginative self.

    """


splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result=splitter.split_text(text)

# print(result)

loader=PyPDFLoader('./code/rag/text splitters/test.pdf')

pdfDocs=loader.load()

# pdfText=''

# for doc in pdfDocs:
#     pdfText+=doc.page_content


# result=splitter.split_text(pdfText)


result=splitter.split_documents(pdfDocs)
print(result)