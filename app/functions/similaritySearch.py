import os

from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def similarity_search(query, k):

    #loading the vectorstore
    embeddings = OpenAIEmbeddings()
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    vectorstore_path = os.path.join(current_directory, "ingester/outputs/faiss_vectorstore")
    vectorstore = FAISS.load_local(vectorstore_path, embeddings)

    #similarity_search for query
    searched_docs = vectorstore.similarity_search(query, k=k)

    return searched_docs


##Test run for similarity_search
# query = "I want to make a zoom meeting"
# vectorstore_path = "faiss_vectorstore"
# docs = similarity_search(query, 2)
# for doc in docs:
#     print(doc.page_content)
#     print('*'*100)
