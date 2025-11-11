# Duckduck Go Search Tool

from langchain_community.tools import DuckDuckGoSearchRun

search_tool=DuckDuckGoSearchRun()

results=search_tool.invoke('Latest news in India')

# print(results)


from langchain_community.tools import  YouTubeSearchTool

search_tool=YouTubeSearchTool()
results=search_tool.invoke('Scoopcast,5')

print(results)
