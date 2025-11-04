# Output

- `Structured output` in LLMs refers to getting the model to generate information in a predefined, machine-readable format (like JSON, XML, YAML, or CSV) rather than free-form natural language text.

- Instead of an LLM simply answering a question, structured output ensures it returns data that adheres to a specific schema, such as a list of items, an object with specific key-value pairs, or a boolean. This is crucial for integrating LLMs into software applications, automating workflows, and enabling reliable programmatic consumption. It's typically achieved through careful prompting, dedicated "JSON modes" in APIs, or libraries that enforce schema validation.


## Typeddict in python

- `TypedDict` in Python is like creating a blueprint for your dictionaries. Instead of just a generic collection of key-value pairs, you define its exact "shape": which keys it *must* have and what *type* of value each key expects (e.g., 'name' is a string, 'age' is an integer).
- This doesn't enforce rules when your code runs, but it helps type checkers (like your IDE) spot mistakes *before* you even hit run. If you try to add a missing key or use the wrong type for a value, you get an immediate warning. It makes your code more predictable, easier to read, and prevents common errors, especially in larger projects where dictionary structures need to be consistent.

- Basically typescript jaisa ( lekin hn koi issue ni aega agar tumne kisi key ko jo integer mang rhi use string de diya lekin han thori readability badh jati hai)


```python
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')


# Schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("The future suddenly sparkled with possibility, bright and inviting. My heart swelled with gratitude and an exhilarating excitement for the journey ahead. This was more than just good news; it was a dream realized, filling me with incredible hope and boundless optimism.")

print(result)

```

### Ismein output kuch aisa ata hai 

{'sentiment': 'positive', 'summary': 'Dream realized, feeling grateful, excited, hopeful, and optimistic about the future.'}

### BTS

- Ek prompt ban jata hai depending upon the variables used in review class
- Wo khud se samjh jata hai ki kya karna hai 
- Jaise summary var se sajmha ke sumaary generate karo
- Sentiment se samjha sentiment generate karo


### Lekin tum a aur b bhi to naam de sakte the??

- Han de sakte lekin fir wo apne aap ni samjhega
- Maine diya tha or ye output ayaa {'a': 'gratitude', 'b': 'optimism'}


### Makes no sense

- To ham is case mein annoted dict bana sakte
- Matlab ham thora sa description de skate varibale ka

```python

class Review(TypedDict):
    summary: Annotated[str,'A brief summary']
    sentiment: Annotated[str,"Return the sentiment of the summary"]

```

### Note

- Ye acha to hai typedDict wala case lekin ismein tum koi validation ni laga sakte

## Pydantic

- Pydantic is a data validation and data parsing library for python. It ensures that the data you work with is correct, structured and type-safe
- Pydantic is smart enough to do the type coercing automatically

- stu_dict={'name':'areeb','age':'24'}
- in class age is a number but pydantic will convert it automatically

## Json Schema 

- Ye bhi use kar sakte

## Difference in all

# Python Data Validation & Schema Tools Comparison

## Quick Comparison Table

| Feature | TypedDict | Pydantic | JSON Schema |
|---------|-----------|----------|-------------|
| **Primary Purpose** | Type hints for dictionaries | Data validation & parsing | Standard JSON validation format |
| **Runtime Validation** | ❌ No | ✅ Full validation | ✅ With external validator |
| **Data Conversion** | ❌ No | ✅ Automatic type coercion | ❌ No |
| **Type Safety** | ✅ Static type checking | ✅ Runtime + static checking | ❌ No native type checking |
| **Performance** | ✅ Zero overhead | ⚠️ Validation overhead | ⚠️ Depends on validator |
| **Dependencies** | ✅ Standard library | ❌ External package | ❌ External validator needed |
| **Cross-Language** | ❌ Python only | ❌ Python only | ✅ Universal standard |
| **Serialization** | ❌ Manual handling | ✅ Built-in methods | ✅ Native JSON |
| **Complex Validation** | ❌ No custom validation | ✅ Rich validators | ✅ Limited with schema |
| **IDE Support** | ✅ Excellent | ✅ Good | ⚠️ Limited without plugins |
| **Learning Curve** | ✅ Very easy | ⚠️ Moderate | ⚠️ Moderate to complex |

## When to Use Each Tool


| Scenario | Tool | 
|---------|-----------|
| Type hints only |	✅ TypedDict |
|Python web APIs	|✅ Pydantic|
|LLM structured output	|✅ Pydantic|
|Cross-language APIs	|✅ JSON Schema|
|Configuration	|✅ Pydantic|
|Quick prototypes	|✅ TypedDict|
|Production systems	|✅ Pydantic|


# Output Parsers

- using_structured_output sare models mein use ni kar sakte
- Jaise mein 1 ghanta waste kiya tha GoogleGenerativeAI model use karte waqt and hf wale models use karte waqt
- To unke liye we use output parsers

- **Output Parsers** in LC help convert raw LLM response into structured formats like JSON,CSV etc

## 4 Major output Parsers

### a) String Output Parser

- returns the output to plain string

### b) JsonOutputParser

- forces the LLM to give json output
- But can't enforce a schema ( matlab main fix ni kar sakta ki keys kya hongi ouput mein)
- Karne ko prompt mein kah sakte lekin koi guarantee ni


### c) StructuredOutputParser

- Schema based output laga sakte without validation ( typeddict jaisa)

### d) PydanticOutputParser
-  Schema based output laga sakte with validation
- Mostly used
