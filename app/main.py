import sys
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project_root) to the Python path
sys.path.append(current_directory)

from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from functions.answer import answer as get_answer

from models import DobbygptAnswerInput

app = FastAPI()

@app.post("/dobbygpt/answer")
def dobbygpt_answer(dobbygptAnswerInput: DobbygptAnswerInput):
    chat_input = dobbygptAnswerInput.dict()
    result = get_answer(chat_input)
    return result
    