from data.questions import QUESTIONS


def get_recommendation(answers):
    # Build lookup tables for O(1) access
    question_lookup = {q.id: q for q in QUESTIONS}

    score = 0
    factors = []

    for answer in answers:
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
            {
                "category": question.category,
                "question": question.text,
                "selected_response": response.text,
                "weight": response.weight,
                "explanation": response.explanation,
            }
        )

    if score >= 10:
        recommendation = "Buy"
    elif score <= -10:
        recommendation = "Rent"
    else:
        recommendation = "Either"

    return {
        "recommendation": recommendation,
        "score": score,
        "factors": factors,
    }