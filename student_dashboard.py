# student_dashboard.py

import tkinter as tk
from tkinter import messagebox

class StudentDashboard:
    def __init__(self, student_id, feedback_messages, creativity_scores, achievements):
        self.student_id = student_id
        self.feedback_messages = feedback_messages
        self.creativity_scores = creativity_scores
        self.achievements = achievements
        self.root = tk.Tk()
        self.root.title(f"Student Dashboard - {self.student_id}")

    def display_dashboard(self):
        # Feedback Section
        feedback_label = tk.Label(self.root, text="Personalized Feedback", font=("Arial", 16))
        feedback_label.pack(pady=10)

        feedback_text = tk.Text(self.root, height=10, width=50)
        feedback_text.pack()
        feedback_text.insert(tk.END, "\n".join(self.feedback_messages))
        feedback_text.config(state='disabled')

        # Creativity Scores Section
        scores_label = tk.Label(self.root, text="Creativity Scores", font=("Arial", 16))
        scores_label.pack(pady=10)

        scores_text = tk.Text(self.root, height=5, width=50)
        scores_text.pack()
        for challenge, score in self.creativity_scores.items():
            scores_text.insert(tk.END, f"{challenge}: {score}\n")
        scores_text.config(state='disabled')

        # Achievements Section
        achievements_label = tk.Label(self.root, text="Achievements", font=("Arial", 16))
        achievements_label.pack(pady=10)

        achievements_text = tk.Text(self.root, height=5, width=50)
        achievements_text.pack()
        achievements_text.insert(tk.END, ", ".join(self.achievements))
        achievements_text.config(state='disabled')

        self.root.mainloop()

if __name__ == "__main__":
    feedback_messages = [
        "Good job! Try exploring more unique ideas to boost your creativity.",
        "Stay engaged! Dive deeper into the challenge to uncover new ideas.",
        "Try to engage more with the task and your peers."
    ]
    creativity_scores = {
        "Challenge 1": 75,
        "Challenge 2": 80,
        "Challenge 3": 70
    }
    achievements = ["Creative Thinker Badge", "Team Player Award"]

    dashboard = StudentDashboard("student_1", feedback_messages, creativity_scores, achievements)
    dashboard.display_dashboard()
