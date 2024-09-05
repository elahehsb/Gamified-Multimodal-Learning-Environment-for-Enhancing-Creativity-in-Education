# app.py (Main API Server using FastAPI)
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import uvicorn

from db import get_db, create_database
from routers import game_challenge, multimodal_data, feedback

app = FastAPI()

# Include different routers for modular APIs
app.include_router(game_challenge.router, prefix="/game")
app.include_router(multimodal_data.router, prefix="/data")
app.include_router(feedback.router, prefix="/feedback")

@app.on_event("startup")
async def startup():
    # Create database tables on startup
    create_database()

@app.get("/")
async def root():
    return {"message": "Welcome to the Gamified Multimodal Learning Environment"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
