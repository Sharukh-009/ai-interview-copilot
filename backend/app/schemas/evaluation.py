from pydantic import BaseModel


class AnswerEvaluation(BaseModel):
    score: float
    feedback: str
    strengths: str
    weaknesses: str