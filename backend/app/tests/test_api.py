from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_questions():
    response = client.get("/questions")

    assert response.status_code == 200

    questions = response.json()

    assert len(questions) == 10
    assert questions[0]["id"] == 1
    assert "responses" in questions[0]


def test_post_recommendation():
    payload = {
        "answers": [
            {"question_id": i, "response_id": 4}
            for i in range(1, 11)
        ]
    }

    response = client.post("/recommendation", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["recommendation"] == "Buy"
    assert data["score"] > 10
    assert len(data["factors"]) == 10