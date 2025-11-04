from typing import TypedDict,Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')


# Schema
class Review(TypedDict):
    summary: Annotated[str,'A brief summary']
    sentiment: Annotated[str,"Return the sentiment of the summary"]

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("The future suddenly sparkled with possibility, bright and inviting. My heart swelled with gratitude and an exhilarating excitement for the journey ahead. This was more than just good news; it was a dream realized, filling me with incredible hope and boundless optimism.")

print(result)