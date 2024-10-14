from pydantic import BaseModel

class DobbygptAnswerInput(BaseModel):
    user_message: str
    files: list = []
    history: list = []