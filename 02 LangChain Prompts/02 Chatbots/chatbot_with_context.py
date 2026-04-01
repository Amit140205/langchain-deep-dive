from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from  langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
chat_history = [
    SystemMessage(content="You are an helpful AI assistant")
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI: ",result.content)

# print(chat_history)