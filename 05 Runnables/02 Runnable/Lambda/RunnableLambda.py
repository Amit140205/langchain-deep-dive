from langchain_core.runnables import RunnableLambda

def count(text):
    return len(text)

text_length_count = RunnableLambda(count)

result = text_length_count.invoke("hello my name is Amit")

print(result)