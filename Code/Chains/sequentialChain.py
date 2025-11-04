# get the topic from user
# LLm give detailed report
# Detailed report se 5 pointers chahiye

from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1=PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)


prompt2=PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

res=chain.invoke({'topic':'cricket'})

print(res)