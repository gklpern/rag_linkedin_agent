from typing import List,Dict,Any

from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from pydantic import BaseModel,Field


class Summary(BaseModel):
    summary:str = Field(description="summary")
    facts:str = Field(description="interesting facts about them")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary,"facts":self.facts}

response_schemas = [
    ResponseSchema(name="summary", description="Short summary about the person"),
    ResponseSchema(name="facts", description="Interesting facts about the person")
]
summary_parser = StructuredOutputParser.from_response_schemas(response_schemas)