from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
import textwrap

# Load environment variables (for the OpenAI API key)
load_dotenv()

# 1️⃣ Initialize LLM (GPT-4o or GPT-4o-mini)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

# 2️⃣ Define the search tool
search_tool = DuckDuckGoSearchRun()

# 3️⃣ Create an agent with tool access
agent = create_agent(
    model=llm,
    tools=[search_tool],
    system_prompt=(
        "You are a helpful news assistant. "
        "Use the search tool to find the latest information about India. "
        "Then summarize your findings into exactly 10 concise bullet points."
    ),
)

# 4️⃣ Run the agent
query = "Top news in India today"
response = agent.invoke({"input": query})

# 5️⃣ Display the summarized output
print("\n🧠 Latest India News Summary:\n")
print(textwrap.fill(response["output"], width=100))
