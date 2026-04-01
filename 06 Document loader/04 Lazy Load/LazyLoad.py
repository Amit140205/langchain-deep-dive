from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dl-curriculum.pdf")

# docs = loader.load()
# loads everything at once

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
