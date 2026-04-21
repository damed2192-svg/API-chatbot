from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Chatbot API")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Chatbot API is running"}
