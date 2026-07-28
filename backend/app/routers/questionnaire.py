from fastapi import APIRouter

from data.questions import QUESTIONS
from models.request import RecommendationRequest
from services.recommendation_engine import get_recommendation

router = APIRouter()


@router.get("/questions")
def get_questions():
    return QUESTIONS


@router.post("/recommendation")
def recommend(request: RecommendationRequest):
    return get_recommendation(request)