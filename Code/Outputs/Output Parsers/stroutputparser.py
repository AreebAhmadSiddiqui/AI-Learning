from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# without stroupuparsers
# template1=PromptTemplate(
#     template='Write a detailed report on {topic}',
#     input_variables=['topic']
# )

# template2=PromptTemplate(
#     template='Write a 5 line summary on the following text:  \n {text}',
#     input_variables=['text']
# )

# prompt1=template1.invoke({'topic':'taj mahal'})
# result1=model.invoke(prompt1)

# prompt2=template2.invoke({'text':result1.content})
# result2=model.invoke(prompt2)

# print(result2.content)


# With strouput parse
from langchain_core.output_parsers import StrOutputParser

template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='Write a 5 line summary on the following text:  \n {text}',
    input_variables=['text']
)

parser= StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':'Taj Mahal'})
print(result)