from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model=GoogleGenerativeAI(model='gemini-2.5-flash')

messages=[
    SystemMessage(content="You are a helpful chat assistant"),
    HumanMessage(content="Tell me about langchain in 100 words")
]

result=model.invoke(messages)

messages.append(AIMessage(content=result))

print(messages)