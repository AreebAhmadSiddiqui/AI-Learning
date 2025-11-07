from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


geminiModel=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Create a loader
loader=TextLoader('./code/RAG/test-text.txt')

document=loader.load()

# print(document)

# [Document(metadata={'source': './code/RAG/test-text.txt'}, page_content='Can you solve this sum ? what is 2+2??')]

prompt=document[0].page_content

print(geminiModel.invoke(prompt).content)