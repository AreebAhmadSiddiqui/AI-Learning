from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests


load_dotenv()

## Tool Creation

@tool
def multiply(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a*b

## Tool Binding

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

llm_with_tools=llm.bind_tools([multiply])

query='What is the multiplication of 2 and 12'
messageHistory=[HumanMessage(content=query)]
## Tool Calling

result=llm_with_tools.invoke(messageHistory)
messageHistory.append(result)
# tool_calls=[{'name': 'multiply', 'args': {'a': 2, 'b': 6}, 'id': '935d9ed5-f771-4597-9fff-4d7c7147ebcd', 'type': 'tool_call'}]

# Send this to LLMs 
result.tool_calls[0]

# Tool Execution

tool_result=multiply.invoke(result.tool_calls[0])
messageHistory.append(tool_result)

#ToolMessage(content='12', name='multiply', tool_call_id='b9e593bf-a6b7-45df-b34a-29be4362d55f')

print(messageHistory)
# LLM call again

print(llm.invoke(messageHistory).content)