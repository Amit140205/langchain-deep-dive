from langchain_core.prompts import PromptTemplate

# template
template = PromptTemplate(
    template="""
        Please summarize the research paper titled "{paper_input}" with the following specification:
        Explaination Style: {style_input}
        Explaination Length: {length_input}
        1. Mathematical Details:
            - Include relevant mathematical equations if present in the paper
            - Exaplain the mathematical concepts using simple, intuitive code snippets where applicable
        2. Analogies:
            - Use relatable analogies to simply complex ideas
        If certain information is not available in the paper, respond with: "Insufficient Information Available" instead of guessing
        Ensure the summery is clear,accurate and aligned with the provided style and length
    """,
    input_variables=["paper_input","style_input","length_input"]
)

template.save("template.json")