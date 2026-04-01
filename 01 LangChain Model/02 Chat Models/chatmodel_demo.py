from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temperature: randomness control parameter
model = ChatOpenAI(model="gpt-4o-mini", temperature=1.5, max_completion_tokens=10)

result = model.invoke("Write a poem on Python")

print(result.content)