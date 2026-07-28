from data.questions import QUESTIONS
from models.request import RecommendationRequest
from models.recommendation import (
    RecommendationFactor,
    RecommendationResponse,
)


def get_recommendation(
    request: RecommendationRequest,
) -> RecommendationResponse:
    question_lookup = {q.id: q for q in QUESTIONS}

    score = 0
    factors: list[RecommendationFactor] = []

    for answer in request.answers:
        question = question_lookup.get(answer.question_id)

        if question is None:
            raise ValueError(f"Question {answer.question_id} does not exist.")

        response = next(
            (r for r in question.responses if r.id == answer.response_id),
            None,
        )

        if response is None:
            raise ValueError(
                f"Response {answer.response_id} does not exist for question {question.id}."
            )

        score += response.weight

        factors.append(
            RecommendationFactor(
                category=question.category,
                weight=response.weight,
                explanation=response.explanation,
            )
        )

    if score >= 10:
        recommendation = "Buy"
    elif score <= -10:
        recommendation = "Rent"
    else:
        recommendation = "Either"

    return RecommendationResponse(
        recommendation=recommendation,
        score=score,
        factors=factors,
    )