from pydantic import BaseModel


class Question(BaseModel):
    question: str
    topic: str
    difficulty: str
    type: str

class AnswerRequest(BaseModel):
    
    
    answer: str