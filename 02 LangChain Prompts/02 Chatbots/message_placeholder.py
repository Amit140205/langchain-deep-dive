from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

# chat prompt template
chat_template = ChatPromptTemplate([
    ("system","You are a helpful customer support assistant"),
    # putting the message placeholder here to feed the context
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")
])
# load chat history
chat_history = []

with open("02 Chatbots/chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})

print(prompt)