from pydantic import BaseModel

class UserResponse(BaseModel):
    question_id: int
    response_id: int