from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summerize the following text {text}",
    input_variables=["text"]
)

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({"topic": "russia vs ukraine"})

print(result)
