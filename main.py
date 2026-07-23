
from fastapi import FastAPI

app = FastAPI(
    title="Coverage Chatbot API",
    version="1.0.0",
    description="Backend API for the Coverage Chatbot"
)


@app.get("/")
def root():
    return {
        "message": "Coverage Chatbot API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }