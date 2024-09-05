# adaptive_feedback_system.py

class AdaptiveFeedbackSystem:
    def __init__(self, student_id):
        self.student_id = student_id

    def provide_feedback(self, creativity_score, emotion, interaction_frequency):
        feedback_messages = []

        # Feedback based on creativity score
        if creativity_score > 80:
            feedback_messages.append("Excellent creativity! Your ideas are innovative and well-expressed.")
        elif 50 <= creativity_score <= 80:
            feedback_messages.append("Good job! Try exploring more unique ideas to boost your creativity.")
        else:
            feedback_messages.append("Consider thinking outside the box to enhance your creativity.")

        # Feedback based on emotion
        if emotion in ["happy", "surprise"]:
            feedback_messages.append("Great to see you're enjoying the challenge!")
        elif emotion in ["sad", "angry"]:
            feedback_messages.append("If you're feeling frustrated, take a short break and return with a fresh perspective.")
        elif emotion == "neutral":
            feedback_messages.append("Stay engaged! Dive deeper into the challenge to uncover new ideas.")

        # Feedback based on interaction frequency
        if interaction_frequency > 0.5:
            feedback_messages.append("You're actively participating. Keep it up!")
        else:
            feedback_messages.append("Try to engage more with the task and your peers.")

        return feedback_messages

if __name__ == "__main__":
    feedback_system = AdaptiveFeedbackSystem("student_1")
    feedback = feedback_system.provide_feedback(
        creativity_score=75,
        emotion="neutral",
        interaction_frequency=0.2
    )
    print("Feedback Messages:")
    for message in feedback:
        print("-", message)
