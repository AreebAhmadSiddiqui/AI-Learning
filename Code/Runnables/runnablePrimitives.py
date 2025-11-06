from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


geminiModel=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

jokeprompt1=PromptTemplate(
    template='Write one joke about {topic}',
    input_variables=['topic']
)

explanationprompt2=PromptTemplate(
    template="Explain the following joke \n {text}",
    input_variables=['text']
)

parser=StrOutputParser()

# 1. Sequential Runnable
from langchain_core.runnables import RunnableSequence

# seqChain= RunnableSequence(prompt1,geminiModel,parser,prompt2,geminiModel,parser)

# print(seqChain.invoke({'topic':'cricket'}))


# 2. Parallel Runnable

# Example -> We need two parallel chains where one model generates tweet and the other linkedin post

from langchain_core.runnables import RunnableParallel
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace

# llm=HuggingFacePipeline.from_model_id(
#     model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation',
#     pipeline_kwargs=dict(
#         temperature=0.5
#     )
# )
# localModel=ChatHuggingFace(llm=llm)


prompt1=PromptTemplate(
    template='Generate a tweet on the topic in 100 words\n {topic}',
    input_variables=['topic']
)


prompt2=PromptTemplate(
    template='Generate a linkedin post on the topic in 100 words\n {topic}',
    input_variables=['topic']
)


parallel_chain=RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1,geminiModel,parser),
        'linkedin':RunnableSequence(prompt2,geminiModel,parser)
    }
)

# print(parallel_chain.invoke({'topic':"AI"}))


# 3. Runnable Passthrough

# topic_for_joke => prompt -> llm -> parser -> Parallel [ RunnablePassthrough , joke_explanation_chain]

from langchain_core.runnables import RunnablePassthrough

# test=RunnablePassthrough()

# print(test.invoke('2')) // outputs 2


joke_gen_chain= RunnableSequence(jokeprompt1,geminiModel,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(explanationprompt2,geminiModel,parser)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

# print(final_chain.invoke({'topic':'AI'}))


# 4. RunnableLambda

# input joke => prompt->llm->parser -- passthrough ( to get the joke)
#                                   -- runnableLambda(to count words in a joke)


from langchain_core.runnables import RunnableLambda

def word_counter(text):
    return len(text.split())

joke_gen_chain= RunnableSequence(jokeprompt1,geminiModel,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'words Count':RunnableLambda(word_counter)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

# print(final_chain.invoke({'topic':'AI'}))


# 5. RunnableBranch

# Practice hai

# Code banao jismein ham ek report lenge user se fir agar usmein 100 words se kam hai to summary generate karenge agar zyada hai to i am sorry cant generate karke response bhej denge

from langchain_core.runnables import RunnableBranch


# 1. Generate a report
report_gen_prompt = PromptTemplate(
    template="""
            You are an expert Essay Writer. Generate an essay on the following topic:

            Topic:
            {topic}

            """,
    input_variables=['topic'])


report_gen_chain =  RunnableSequence(report_gen_prompt,geminiModel,parser)

# print(report_gen_chain.invoke({'topic':'AI'}))

summary_prompt = PromptTemplate(template="""
You are an expert summarizer. Create a concise summary of the following report:

REPORT:
{text}

Please provide a clear and concise summary in 100-150 words.
""",input_variables=['text'])


def isWordGreaterThan500(text):
    return len(text.split())>=500

branch_chain = RunnableBranch(
    (isWordGreaterThan500, RunnableSequence(summary_prompt,geminiModel,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

print(final_chain.invoke({'topic':"Russia vs Ukraine"}))

