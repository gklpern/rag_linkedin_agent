from dotenv import load_dotenv

load_dotenv()
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

from langchain import hub   
from tools.tools import get_profile_url_tavily




def lookup(name:str) -> str:

    llm=ChatOllama(
        temperature=0,
        model='llama3.2:latest'
    )

    template=""" given the full name {name_of_person} I want you to get it me a link to their linkedin profile page.
                Your answer should contain only a URL"""
    

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True , handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format(name_of_person=name)}

    )

    linked_profile_url = result["output"]
    return linked_profile_url



if __name__ == "__main__":
    result = lookup("Gökalp Eren Akol")
    print(result)