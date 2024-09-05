# routers/multimodal_data.py
from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from db import get_db, MultimodalData
import json
import time

router = APIRouter()

@router.post("/upload")
async def upload_data(
    user_id: int = Form(...),
    data_type: str = Form(...),  # e.g., 'text', 'image', 'audio'
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Process file (e.g., store it in filesystem, analyze, etc.)
    file_content = await file.read()
    # Save file metadata and contents into the database
    multimodal_data = MultimodalData(
        user_id=user_id,
        data_type=data_type,
        data_content=file_content.decode("utf-8"),
        timestamp=time.time()
    )
    db.add(multimodal_data)
    db.commit()
    return {"message": "Data uploaded successfully"}
