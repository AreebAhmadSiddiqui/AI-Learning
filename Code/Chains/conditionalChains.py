# Get a feedback
# Analyze for pos/neg
# for postive reply with graceful message
# for negative reply with what we can do better etc

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

strParser=StrOutputParser()

class Sentiment(BaseModel):
    sentiment : Literal['positive','negative']=Field(description='Give the sentiment of the feedback')

pydanticParser=PydanticOutputParser(pydantic_object=Sentiment)

prompt1=PromptTemplate(
    template='Classify the sentiment of the following text into positive and negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':pydanticParser.get_format_instructions()}
)

classifier_chain = prompt1 | model | pydanticParser
## stroutputparser se to wo positive negative de raha hai lekin zaruri ni hai we want to get fixed value so we should use pydanticOutputParser


# res=classifier_chai.invoke({'feedback':'This is a terrible smartphone'})

# print(res.sentiment)

# For branches we use RunnableBranch


prompt2=PromptTemplate(
    template='Write one natural response to this positive feedback in one sentence\n {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='Write one natural response to this negative feedback in one sentence\n {feedback}',
    input_variables=['feedback']
)


branch_chain=RunnableBranch(
    (lambda x : x.sentiment == 'positive' , prompt2 | model | strParser),
    (lambda x : x.sentiment == 'negative' , prompt3 | model | strParser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

final_chain=classifier_chain | branch_chain

res=final_chain.invoke({'feedback':'This is a trash phone'})

print(res)

# For the graph
final_chain.get_graph().print_ascii()