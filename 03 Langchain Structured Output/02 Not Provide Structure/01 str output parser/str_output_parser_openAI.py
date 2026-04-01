from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# 1st prompt
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
prompt1 = template1.invoke({
    "topic": "blackhole"
})
result = model.invoke(prompt1)
# print("Detailed Report : ",result.content)

# 2nd prompt
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text \n {text}",
    input_variables=["text"]
)
prompt2 = template2.invoke({
    "text": result.content
})
ans = model.invoke(prompt2)
print("Summary : ",ans.content)