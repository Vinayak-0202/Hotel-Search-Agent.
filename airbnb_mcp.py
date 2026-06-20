import sys
import  os
from dotenv import load_dotenv
load_dotenv() 

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage 

from scripts import base_tools, prompts

from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

#Set UTF-8 encoding for Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

async def get_tools():
    client = MultiServerMCPClient(
    {
        "airbnb": {
        "command": "npx",
        "args": [
            "-y",
            "@openbnb/mcp-server-airbnb",
            "--ignore-robots-txt"
        ],
        "transport": "stdio"
        }
    }
    )
    
    mcp_tools = await client.get_tools()
    tools = mcp_tools + [base_tools.web_search, base_tools.get_weather]
    #print(f"Tools available: {tools}")
    return tools

async def hotel_search(query: str):
    tools = await get_tools() 
    agent  = create_agent(
        model=model,
        tools=tools,
        system_prompt=prompts.AIRBNB_PROMPT,
    )

    result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
    response = result['messages'][-1].text
    print("=========Output=========")
    print(response)
    

async def ask():
    print("\n\nChat mode startded. Type 'q' or 'quite' to exit.")
    while True: 
        print("\n\n\nAsk Another Question. Type 'q' or 'quite' to exit.")
        query = input("You: ").strip()

        if query.lower() in ["q", "quite"]:
            print("Exiting chat mode.")
            break

        await hotel_search(query)

if __name__ == "__main__":
    asyncio.run(ask())