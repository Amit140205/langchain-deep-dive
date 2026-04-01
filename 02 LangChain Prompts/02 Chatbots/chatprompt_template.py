from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# dynamically manage the chat prompt
chat_template = ChatPromptTemplate([
    ("system","You are a helpful {domain} expert"),
    ("human","Explain in simple terms, what is {topic}")
    # this does not work like these
    # SystemMessage(content="You are a helpful {domain} expert"),
    # HumanMessage(content="Explain in simple terms, what is {topic}?")
])

prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "lbw"
})

print(prompt)

