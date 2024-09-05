# routers/feedback.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db, MultimodalData
from tasks import analyze_facial_expression, analyze_text_sentiment, analyze_creativity_score

router = APIRouter()

@router.get("/{user_id}")
def get_feedback(user_id: int, db: Session = Depends(get_db)):
    data = db.query(MultimodalData).filter(MultimodalData.user_id == user_id).all()
    
    # Run analysis in background tasks
    if data:
        last_data = data[-1]  # Get the latest data
        feedback = []

        if last_data.data_type == "text":
            creativity_score = analyze_creativity_score(last_data.data_content)
            sentiment = analyze_text_sentiment(last_data.data_content)
            feedback.append(f"Creativity Score: {creativity_score}")
            feedback.append(f"Sentiment Analysis: {sentiment}")
        # Add analysis for other data types like 'image', 'audio'

        return {"feedback": feedback}
    return {"message": "No data available"}
