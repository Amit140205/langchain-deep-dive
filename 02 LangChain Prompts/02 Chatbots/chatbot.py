from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
# this maintains the chat history
chat_history = []
while True:
    # here a basic problem is that, LLM does not have context of the previous messages
    # user_input = input("You: ")
    # if user_input == "exit":
    #     break
    # result = model.invoke(user_input)
    # print("AI: ",result.content)

    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print(result.content)
    # problem in this approach is that
    # as the chat_history grows constantly, it will be difficult for a LLM as well as us to classfy
    # the messages which one is ours and which one is AI's

print(chat_history)