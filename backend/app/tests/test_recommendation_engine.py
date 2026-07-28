import pytest

from app.models.request import Answer, RecommendationRequest
from app.services.recommendation_engine import get_recommendation


def test_buy_recommendation():
    request = RecommendationRequest(
        answers=[
            Answer(question_id=i, response_id=4)
            for i in range(1, 11)
        ]
    )

    result = get_recommendation(request)

    assert result.recommendation == "Buy"
    assert result.score > 10
    assert len(result.factors) == 10


def test_rent_recommendation():
    request = RecommendationRequest(
        answers=[
            Answer(question_id=i, response_id=1)
            for i in range(1, 11)
        ]
    )

    result = get_recommendation(request)

    assert result.recommendation == "Rent"
    assert result.score < -10
    assert len(result.factors) == 10


def test_neutral_recommendation():
    request = RecommendationRequest(
        answers=[
            Answer(question_id=1, response_id=2),
            Answer(question_id=2, response_id=2),
            Answer(question_id=3, response_id=2),
            Answer(question_id=4, response_id=3),
            Answer(question_id=5, response_id=3),
            Answer(question_id=6, response_id=2),
            Answer(question_id=7, response_id=3),
            Answer(question_id=8, response_id=2),
            Answer(question_id=9, response_id=2),
            Answer(question_id=10, response_id=3),
        ]
    )

    result = get_recommendation(request)

    assert result.recommendation == "Either"


def test_invalid_question():
    request = RecommendationRequest(
        answers=[
            Answer(question_id=99, response_id=1)
        ]
    )

    with pytest.raises(ValueError):
        get_recommendation(request)


def test_invalid_response():
    request = RecommendationRequest(
        answers=[
            Answer(question_id=1, response_id=99)
        ]
    )

    with pytest.raises(ValueError):
        get_recommendation(request)