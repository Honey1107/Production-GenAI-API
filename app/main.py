from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, chat


app = FastAPI(
    title="Day 10 - Production GenAI API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)


app.include_router(auth.router)
app.include_router(chat.router)


@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }


@app.get("/")
async def root():

    return {
        "message": "Production GenAI API is running"
    }
