from pydantic import BaseModel

class ResponseOption(BaseModel):
    id: int
    text: str
    weight: int
    explanation: str
    
class Question(BaseModel):
    id: int
    text: str
    category: str
    responses: list[ResponseOption]
