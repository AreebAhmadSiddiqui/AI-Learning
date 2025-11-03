from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    # max_new_tokens=100,
    do_sample=False,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Write an essay on India in 200 words")
print(result.content)
