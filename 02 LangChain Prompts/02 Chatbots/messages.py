from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")
# three types of messages are there : 
# 1. System message
# 2. Human message
# 3. AI message

messages = [
    SystemMessage(content="You are a helpful AI assistant"),
    HumanMessage(content="Tell me about langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)