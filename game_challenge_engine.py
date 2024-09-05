# game_challenge_engine.py

import json
import random

class GameChallengeEngine:
    def __init__(self):
        self.challenges = self.load_challenges()
        self.active_challenges = {}

    def load_challenges(self, filepath='challenges.json'):
        try:
            with open(filepath, 'r') as file:
                challenges = json.load(file)
            return challenges
        except FileNotFoundError:
            print("Challenges file not found. Loading default challenges.")
            return self.default_challenges()

    def default_challenges(self):
        # Define some default challenges
        return [
            {
                "id": 1,
                "title": "The Eco City Project",
                "description": "Design a sustainable city using renewable energy sources.",
                "subjects": ["Science", "Geography"],
                "difficulty": "Medium",
                "group_size": 4
            },
            {
                "id": 2,
                "title": "Mathematical Treasure Hunt",
                "description": "Solve a series of math puzzles to find the hidden treasure.",
                "subjects": ["Math"],
                "difficulty": "Easy",
                "group_size": 2
            },
            # Add more challenges as needed
        ]

    def assign_challenge(self, challenge_id, student_ids):
        challenge = next((c for c in self.challenges if c["id"] == challenge_id), None)
        if challenge:
            self.active_challenges[challenge_id] = {
                "challenge": challenge,
                "students": student_ids,
                "status": "Active"
            }
            print(f"Assigned challenge '{challenge['title']}' to students {student_ids}.")
        else:
            print(f"Challenge with ID {challenge_id} not found.")

    def get_active_challenges(self):
        return self.active_challenges

if __name__ == "__main__":
    engine = GameChallengeEngine()
    engine.assign_challenge(1, ["student_1", "student_2", "student_3", "student_4"])
    print("Active Challenges:", engine.get_active_challenges())
