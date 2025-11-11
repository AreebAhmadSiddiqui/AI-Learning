# Custom tool using @tool

# Three Steps Process for custom tools

from langchain_core.tools import tool

# Step 1 Create a tool

def multiply(a,b):
    """Multiply two numbers"""
    return a*b

# Step 2 add type hints

def multiply(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a*b


# Step 3 add tool decorator

@tool
def multiply(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a*b


print(multiply.invoke({'a':1,'b':20}))


# Not just a normal function

print(multiply.name)  # multiply
print(multiply.description) # Multiply two numbers
print(multiply.args) # {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}


# To LLM we send schema

print(multiply.args_schema.model_json_schema())

## Ouput
{
  "description": "Multiply two numbers",
  "properties": {
    "a": {
      "title": "A",
      "type": "integer"
    },
    "b": {
      "title": "B",
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ],
  "title": "multiply",
  "type": "object"
}


# Second Method For Tool creation ( using StructuredTool & Pydantic)
# More strict

from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field

# Pydantic Class

class MultiplyInput(BaseModel):
    a: int = Field(required=True,description='The first number to add')
    b: int = Field(required=True,description='The second number to add')


def multiply_func(a:int,b:int) -> int:
    return a*b


multiply_tool=StructuredTool.from_function(
    func=multiply_func,
    name='multiply',
    description='Multiply two numbers',
    args_schema=MultiplyInput
)

result=multiply_tool.invoke({'a':3,'b':5})

print(result)