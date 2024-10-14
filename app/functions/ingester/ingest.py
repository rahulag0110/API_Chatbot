import os

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def ingest():
    
    #Getting the text files in the inputs folder
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(current_directory, 'inputs')
    input_files = os.listdir(input_folder)
    
    #Creating the output folder if it doesn't exist
    output_folder = os.path.join(current_directory, 'outputs')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    ###Improve Later###
    #Now the code is only for one text file
    file_path = os.path.join(input_folder, input_files[0])
    loader = TextLoader(file_path)
    doc = loader.load()

    #Splitting the document into chunks
    splitter = CharacterTextSplitter(
        separator="----------------------------------------------------------------------------------------------",
        chunk_size = 0,
        chunk_overlap = 0
    )
    splitted_docs = splitter.split_documents(doc)
    
    #Embedding the chunks to create the vector store with FAISS and saving in the outputs folder
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(splitted_docs, embeddings)
    vectorstore.save_local(os.path.join(output_folder, 'faiss_vectorstore'))

if __name__ == "__main__":
    ingest()