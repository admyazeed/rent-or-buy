from pydantic import BaseModel


class RecommendationFactor(BaseModel):
    category: str
    weight: int
    explanation: str


class RecommendationResponse(BaseModel):
    recommendation: str
    score: int
    factors: list[RecommendationFactor]