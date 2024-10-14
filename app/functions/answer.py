import sys
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory (project_root) to the Python path
sys.path.append(current_directory)

from promptgen import prompt_generator
from similaritySearch import similarity_search

from langchain.chat_models import ChatOpenAI

def answer(chat_input):
    
    user_message = chat_input["user_message"]
    
    searched_docs = similarity_search(user_message, 2)
    
    llm = ChatOpenAI(temperature = 0, model = "gpt-3.5-turbo")
    prompt = prompt_generator(searched_docs, chat_input)
    
    answer = llm(prompt)
    
    return answer

# answer = answer(
#     chat_input = {
#         "user_message": "Please make a QR code for the following URL: sell_anything.com",
#         "files": ["a.pdf", "cooking_show.mp4", "c.pdf", "b.pdf", "spiderman.mp4"],
#         "history": []
#     },
# )
# print(answer.content)