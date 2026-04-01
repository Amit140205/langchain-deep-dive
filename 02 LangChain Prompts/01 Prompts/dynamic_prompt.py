from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
# importing the prompt template from langchain
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

st.header("Research Tool")

# now we are going to create 3 dropdowns
paper_input = st.selectbox("Select Research Paper Name",["Select...","Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: Language Models are Few Shot Learners","Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explaination Style",["Beginner-Friendly","Technical","Code-Oriented","Mathematical"])

length_input = st.selectbox("Select Exaplaination Length",["Short (1-2 paragraphs)","Medium (3-5 paragraphs)","Long (detailed explaination)"])

# template
# template = PromptTemplate(
#     template="""
#         Please summarize the research paper titled "{paper_input}" with the following specification:
#         Explaination Style: {style_input}
#         Explaination Length: {length_input}
#         1. Mathematical Details:
#             - Include relevant mathematical equations if present in the paper
#             - Exaplain the mathematical concepts using simple, intuitive code snippets where applicable
#         2. Analogies:
#             - Use relatable analogies to simply complex ideas
#         If certain information is not available in the paper, respond with: "Insufficient Information Available" instead of guessing
#         Ensure the summery is clear,accurate and aligned with the provided style and length
#     """,
#     input_variables=["paper_input","style_input","length_input"]
# )

# this approach is helpful for smaller prompts but for long size prompts, we can save the prompt in a separate file(reusable) the load it here

template = load_prompt("template.json")

# fill the placeholders
# prompt = template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input
# })


# if st.button("Summarize"):
#     result = model.invoke(prompt)
#     st.write(result.content)

# in the above approach, we twice use invoke 
# but this can be simplified by using a "chain"

if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.write(result.content)