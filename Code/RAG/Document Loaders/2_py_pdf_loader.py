from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


geminiModel=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Create a loader
loader=PyPDFLoader('./code/RAG/GenAI.pdf')

document=loader.load()

textContent=''

for doc in document:
    textContent+=doc.page_content+' '

print(textContent)