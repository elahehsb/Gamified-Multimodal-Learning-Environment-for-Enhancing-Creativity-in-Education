from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db, Challenge

router = APIRouter()

@router.get("/list")
def get_challenges(db: Session = Depends(get_db)):
    return db.query(Challenge).all()

@router.post("/create")
def create_challenge(title: str, description: str, db: Session = Depends(get_db)):
    new_challenge = Challenge(title=title, description=description)
    db.add(new_challenge)
    db.commit()
    return {"message": f"Challenge '{title}' created successfully."}
