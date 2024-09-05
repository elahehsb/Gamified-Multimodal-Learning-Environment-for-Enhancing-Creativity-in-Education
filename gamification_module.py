# gamification_module.py

class GamificationModule:
    def __init__(self):
        self.student_points = {}
        self.badges = {
            "Creative Thinker": 100,
            "Team Player": 80,
            "Innovator": 120
        }
        self.leaderboard = []

    def award_points(self, student_id, points):
        self.student_points[student_id] = self.student_points.get(student_id, 0) + points
        print(f"Awarded {points} points to {student_id}. Total points: {self.student_points[student_id]}")

    def check_for_badges(self, student_id):
        total_points = self.student_points.get(student_id, 0)
        earned_badges = [badge for badge, threshold in self.badges.items() if total_points >= threshold]
        print(f"{student_id} has earned badges: {earned_badges}")
        return earned_badges

    def update_leaderboard(self):
        self.leaderboard = sorted(self.student_points.items(), key=lambda x: x[1], reverse=True)
        print("Leaderboard updated.")

    def display_leaderboard(self):
        print("Leaderboard:")
        for rank, (student_id, points) in enumerate(self.leaderboard, start=1):
            print(f"{rank}. {student_id} - {points} points")

if __name__ == "__main__":
    gamification = GamificationModule()
    gamification.award_points("student_1", 50)
    gamification.award_points("student_2", 120)
    gamification.award_points("student_1", 60)
    gamification.check_for_badges("student_1")
    gamification.update_leaderboard()
    gamification.display_leaderboard()
