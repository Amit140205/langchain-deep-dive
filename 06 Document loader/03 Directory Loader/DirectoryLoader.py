from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    path="DemoDir",
    glob="*.txt",
    loader_cls=TextLoader
)

docs = loader.load()

print(docs)
print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)