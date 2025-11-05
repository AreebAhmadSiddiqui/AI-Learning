import random

# ## Case 1 - Jo langchain walon ne pehle kiya har use case ka ek chain Component 


# # Nakli LLM class ( which behaves like LLM)
# class NakliLLM:
#     def __init__(self):
#         print("LLM created")
#     def predict(self,prompt):
#         response_list=[
#             'first res',
#             'second res',
#             'third res'
#         ]
#         return {'response':random.choice(response_list)}

# # llm=NakliLLM()

# # print(llm.predict('test'))


# # Nakli PromptTemplate class ( which behaves like PromptTemplate)
# class NakliPromptTemplate:
#     def __init__(self,template,input_variables):
#         self.template=template
#         self.input_variables=input_variables
#     def format(self,input_dict):
#         return self.template.format(**input_dict)

#     ## Agar ye function samjh ni aya hai to ye karta hai dekho template ek string hai usmein format function se seedhe ` ` wala kaam kar sakte

#     ## 'hello {}'.format('Areeb') -> areeb wahan chala jaege
#     ## Dictionary ke case mein Ex- dict = {'name':'Areeb' }  str = 'hello {name}'.format(**dict) => 'hello {name}.format(name=Areeb) aisa ho jaeaga
#     ## Hn obviously names placeholders match hone chahiye
#     #person = {'name': 'Bob', 'age': 25}
#     # Using key names directly
#     #text = "Hello {name}, you are {age} years old".format(**person)
#     #print(text)
#     # Output: Hello Bob, you are 25 years old

# class NakliLLMChain:
#     def __init__(self,prompt,llm):
#         self.llm=llm
#         self.prompt=prompt
#     def run(self,input_dict):
#         final_prompt=self.prompt.format(input_dict)
#         result=self.llm.predict(final_prompt)
#         return result['response']

# template=NakliPromptTemplate(
#     'Give me a summary on this topic \n {topic}',
#     input_variables=['topic']
# )

# # get the prompt
# prompt=template.format({'topic':'AI'})

# # # Create LLM
# # llm=NakliLLM()

# # # Pass this prompt to LLM
# # res=llm.predict(prompt=prompt)

# # print(res)

# # Or 

# # Chain concept
# chain=NakliLLMChain(prompt,llm)
# print(chain.run({'topic':'AI'}))

## Ye to bahut complex ho gyaa kitni sari class banani padegi har class ka alag method invoke kisi ka , kisi ka predict , kisi ka format ko consistency hi ni
## Consistency kaise aegi??? ( Hint : OOPS concept ????)
## Sahi kaha Abstraction se aegi ( Main agar ek abstract class bana do aur sabhi generic class unse derive ho to ek common function to sabko bana hoga hainaaa!!!! yes lets create it)
## Also kyunki mujhe ek ka input doosre ka output banana hai main un sabhi ko ek connector class se connect kardunga

# Case 2 
from abc import ABC,abstractmethod

class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass

# Nakli LLM class ( which behaves like LLM)
class NakliLLM(Runnable):
    def __init__(self):
        print("LLM created")

    def invoke(self,prompt):
        response_list=[
            'first res',
            'second res',
            'third res'
        ]
        return {'response':random.choice(response_list)}

    # Inform user that this predict method will deprecate
    def predict(self,prompt):
        response_list=[
            'first res',
            'second res',
            'third res'
        ]
        return {'response':random.choice(response_list)}
        

# Nakli PromptTemplate class ( which behaves like PromptTemplate)
class NakliPromptTemplate(Runnable):
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables
    def invoke(self,input_dict):
        return self.template.format(**input_dict)

    # Inform user that this format method will deprecate
    def format(self,input_dict):
        return self.template.format(**input_dict)

## AB kya hua ek common method to a gaya bhai

## Lets create a class to connect these two

class RunnableConnector(Runnable):
    def __init__(self,runnable_list):
        self.runnable_list=runnable_list
    def invoke(self,input_data):
        # Yahan dekho kya ho rha hai

        # Run chala (with a ip) -> gets an output -> ab wo doosre ka input banega na to kya karoge -> input_data variable output store karlo 
        for runnable in self.runnable_list:
            input_data=runnable.invoke(input_data)
        
        return input_data


template=NakliPromptTemplate(
    'Give me a summary on this topic \n {topic}',
    input_variables=['topic']
)

# Create LLM
llm=NakliLLM()


## lets say ek parser bhi chahiye instead of this ouput {'response': 'second res'} i want just the key

class NakliStrOpParser(Runnable):
    def invoke(self,input):
        return input['response']

parser=NakliStrOpParser()
chain = RunnableConnector([template,llm,parser])


res=chain.invoke({'topic':'AI'})
print(res)


## Congo you created Runnables from scratch


## Practice ( Two chains combined together)

# - Ek chain topic pe summary gen karti hai
# - Doosri us summary ki qna

template1=NakliPromptTemplate(
    'Give me a summary on this topic \n {topic}',
    input_variables=['topic']
)

llm1=NakliLLM()

chain1 = RunnableConnector([template1,llm1])


template2=NakliPromptTemplate(
    'Give me a qna on this text \n {response}',
    input_variables=['response']
)
llm2=NakliLLM()

chain2=RunnableConnector([template2,llm2])

finalChain=RunnableConnector([chain1,chain2])

print(finalChain.invoke({'topic':"Hello"}))

# Congoo you build this too