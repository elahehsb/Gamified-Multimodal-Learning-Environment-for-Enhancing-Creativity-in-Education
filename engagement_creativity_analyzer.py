# engagement_creativity_analyzer.py

from deepface import DeepFace
from textblob import TextBlob
import cv2

class EngagementCreativityAnalyzer:
    def __init__(self, student_id):
        self.student_id = student_id

    def analyze_facial_expression(self, image_path):
        try:
            analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
            emotion = analysis['dominant_emotion']
            print(f"Detected emotion: {emotion}")
            return emotion
        except Exception as e:
            print(f"Facial analysis failed: {e}")
            return None

    def analyze_text_input(self, text_input):
        creativity_score = self.assess_creativity(text_input)
        sentiment = TextBlob(text_input).sentiment.polarity
        print(f"Text sentiment polarity: {sentiment}")
        return {
            "creativity_score": creativity_score,
            "sentiment": sentiment
        }

    def assess_creativity(self, text):
        # Simple heuristic: longer, diverse vocabulary indicates higher creativity
        words = text.split()
        unique_words = set(words)
        creativity_score = len(unique_words) / len(words) * 100 if words else 0
        print(f"Creativity score: {creativity_score}")
        return creativity_score

    def analyze_interaction_patterns(self, interaction_log):
        # Analyze interaction patterns for engagement
        total_interactions = len(interaction_log)
        interaction_frequency = total_interactions / (interaction_log[-1]['timestamp'] - interaction_log[0]['timestamp'] + 1)
        print(f"Interaction frequency: {interaction_frequency} interactions per second")
        return interaction_frequency

if __name__ == "__main__":
    analyzer = EngagementCreativityAnalyzer("student_1")
    emotion = analyzer.analyze_facial_expression("data/student_1_frame.jpg")
    text_analysis = analyzer.analyze_text_input("Once upon a time, there was a brave knight who fought dragons.")
    print("Text Analysis:", text_analysis)
