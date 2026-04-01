from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# task
# topic -> LLM -> detailed analysis -> LLM -> prompt
# this does not work due to hugging face issue
# though the code absolutely correct

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
prompt1 = template1.invoke({
    "topic": "blackhole"
})

result = model.invoke(prompt1)

# 2nd prompt
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text \n {text}",
    input_variables=["text"]
)
prompt2 = template2.invoke({
    "text": result.content
})


ans = model.invoke(prompt2)

print(ans.content)