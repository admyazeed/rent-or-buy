from fastapi import FastAPI

from routers.questionnaire import router

app = FastAPI()

app.include_router(router)