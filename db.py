# db.py (Database Configuration and Models)
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/learning_db"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create models for Users, Challenges, and Collected Data
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Challenge(Base):
    __tablename__ = "challenges"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)

class MultimodalData(Base):
    __tablename__ = "multimodal_data"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    data_type = Column(String)  # e.g., 'text', 'image', 'audio'
    data_content = Column(Text)  # Store data as JSON or other format
    timestamp = Column(Float)

def create_database():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
