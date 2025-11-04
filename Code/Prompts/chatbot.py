from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model=GoogleGenerativeAI(model='gemini-2.5-flash')


chat_his=[
    SystemMessage(content="You are a helpful chat assistant")
]

while True:
    user_input=input('You:  ')+" max 100 words"
    chat_his.append(HumanMessage(content=user_input))
    if user_input.count('exit')!=0:
        break
    result=model.invoke(chat_his)
    chat_his.append(AIMessage(content=result))
    print("AI :",result)

print(chat_his)