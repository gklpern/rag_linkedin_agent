from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import Tuple

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser, Summary


def ice_break_with(name: str) -> Tuple[Summary, str]:

    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock=True)


    summary_template = """
        Given the LinkedIn information below, please extract and return a JSON object with the following format:

        {format_instructions}

        LinkedIn information:
        {information}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=['information'],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        }
    )

    llm = ChatOllama(model='llama3.2:latest')
    chain = summary_prompt_template | llm | summary_parser


    res: Summary = chain.invoke(input={'information': linkedin_data})

    return res, linkedin_data.get('photoUrl')


if __name__ == '__main__':
    load_dotenv()
    print('ice breaker entering')
    ice_break_with(name="Eden Marco")
