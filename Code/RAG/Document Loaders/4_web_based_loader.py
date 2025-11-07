from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


geminiModel=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

url='https://en.wikipedia.org/wiki/LangChain'
loader=WebBaseLoader(url)

docs=loader.load()

text=docs[0].page_content

prompt=PromptTemplate(
    template='Generate a summary of this text \n {text}',
    input_variables=['text']
)

chain = prompt | geminiModel | StrOutputParser()

print(chain.invoke(text))