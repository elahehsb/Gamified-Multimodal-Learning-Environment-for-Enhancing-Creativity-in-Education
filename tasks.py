 (Celery Worker)
from celery import Celery
from deepface import DeepFace
from textblob import TextBlob
import json

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def analyze_facial_expression(image_path):
    analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    return analysis

@celery_app.task
def analyze_text_sentiment(text_input):
    sentiment = TextBlob(text_input).sentiment.polarity
    return sentiment

@celery_app.task
def analyze_creativity_score(text_input):
    words = text_input.split()
    unique_words = set(words)
    creativity_score = len(unique_words) / len(words) * 100 if words else 0
    return creativity_score
