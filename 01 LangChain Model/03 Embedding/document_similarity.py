from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# performing document simlarity search

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small',dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'Tell me about Rohit Sharma'

# document embedding
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# performing cosine similarity(takes 2D array as an input always)
scores = cosine_similarity([query_embedding],doc_embeddings)[0] # returns a 2D array

print(scores) # [0.65690122 0.41304807 0.34305172 0.38224346 0.35180236]
# now we have to extract the highest similarity
# for that we have to sort then extract the last index item

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(documents[index])
print("Similarity score : ", score)

