from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model=GoogleGenerativeAI(model='gemini-2.5-flash')

while True:
    user_input=input('You:  ')+"in 100 words"
    if user_input == 'exit':
        break
    result=model.invoke(user_input)
    print("AI :",result)
