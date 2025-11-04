from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


# chat template
chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),

    # Yahan pe sare previous history store kardo

    MessagesPlaceholder(variable_name='chat_history'),

    ('human','{query}')
])

chat_history=[]

# Load chat history
with open('./Prompts/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

prompt=chat_template.invoke({'chat_history':chat_history,'query':'Where is my refund'})

print(prompt)