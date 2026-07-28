from pydantic import BaseModel


class Answer(BaseModel):
    question_id: int
    response_id: int


class RecommendationRequest(BaseModel):
    answers: list[Answer]