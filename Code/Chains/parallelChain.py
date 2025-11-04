# Given a piece of information

# - One chain generates notes
# - The other chain generates quiz
# - and finally combine these two to give the final output


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

# for Notes
model1=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

llm= HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    # max_new_tokens=100,
    do_sample=False,
)

# For Quiz
model2 = ChatHuggingFace(llm=llm)


prompt1=PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='Generate a quiz of 5 question from the following text \n {text}',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template="Merge the following documents into a single document \n notes -> {notes} and \n quiz -> {quiz} ",
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        'notes': prompt1 | model1 | parser,
        'quiz': prompt2 | model2 | parser
    }
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

res= chain.invoke({'text':"""Large Language Models (LLMs) represent one of the most transformative technological advancements of the digital age. At their core, LLMs are sophisticated artificial intelligence systems trained on vast quantities of textual data from the internet, enabling them to understand, generate, and manipulate human language with remarkable proficiency. Models like GPT-4, Gemini, and Llama are not merely programmed with rules; they learn patterns, contexts, and nuances by analyzing billions of sentences, allowing them to write essays, translate languages, write code, and answer complex questions. This capability is reshaping industries and redefining human-computer interaction.

The potential benefits of LLMs are profound. In education, they can act as personalized tutors, providing instant explanations and generating practice materials. In healthcare, they can sift through medical research to assist with diagnostics and patient communication. For creativity, they are powerful co-pilots, helping writers, marketers, and designers brainstorm ideas and draft content. Perhaps their most significant impact is in democratizing access to information and automation. Small businesses can now generate professional marketing copy or legal documents without hiring expensive agencies, and individuals can get detailed answers to complex queries in seconds, breaking down barriers to knowledge.

However, this immense power is accompanied by significant challenges and risks. A primary concern is the problem of "hallucination," where LLMs generate plausible but entirely fabricated information with unwavering confidence. This poses a grave threat to the reliability of information, blurring the lines between fact and fiction. Furthermore, because these models are trained on data created by humans, they inevitably inherit and can amplify societal biases present in that data, potentially perpetuating stereotypes related to race, gender, and culture.

The ethical implications are equally pressing. The use of copyrighted material in training datasets raises complex legal questions about intellectual property and fair use. The ability of LLMs to generate human-like text also fuels the proliferation of misinformation and disinformation at an unprecedented scale, making it easier to create convincing fake news, fraudulent reviews, and malicious phishing emails. Moreover, the automation of content creation threatens to disrupt countless jobs in writing, customer service, and other language-centric fields, necessitating a societal conversation about economic displacement and reskilling.

In conclusion, Large Language Models are a technological double-edged sword. They offer a future of increased efficiency, creativity, and accessibility, holding the promise of augmenting human intelligence and streamlining complex tasks. Yet, they also introduce formidable risks related to misinformation, bias, and ethical ambiguity. Navigating this new landscape requires more than just technological innovation; it demands robust ethical frameworks, transparent development practices, and continuous public discourse. The future shaped by LLMs will ultimately depend not on the models themselves, but on the wisdom, responsibility, and foresight of the humans who guide their development and deployment."""})

print(res)