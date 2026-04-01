from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch,RunnableLambda

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

class Feedback(BaseModel):
    sentiment: Literal["positive","negetive"] = Field(description="Give the sentiment of the feedback")

parser = PydanticOutputParser(pydantic_object=Feedback)
parser1 = StrOutputParser()

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negetive \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser

# result = classifier_chain.invoke({
#     "feedback": "this is a terrible smartphone"
# })

# print(result)

# classification done

# branching it into positive or negetive

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)
prompt3 = PromptTemplate(
    template="Write an appropriate response to this negetive feedback \n {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    # (condition1, chain)
    (lambda x: x.sentiment == "positive", prompt2 | model | parser1),
    # (condition2, chain)
    (lambda x: x.sentiment == "negetive", prompt3 | model | parser1),
    # (default chain)
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({
    "feedback": "this is a terrible smartphone"
})

print(result)