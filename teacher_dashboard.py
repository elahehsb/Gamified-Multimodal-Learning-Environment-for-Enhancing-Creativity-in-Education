# teacher_dashboard.py

import tkinter as tk
from tkinter import ttk

class TeacherDashboard:
    def __init__(self, class_data):
        self.class_data = class_data
        self.root = tk.Tk()
        self.root.title("Teacher Dashboard")

    def display_dashboard(self):
        tree = ttk.Treeview(self.root)
        tree['columns'] = ('Creativity Score', 'Engagement Level', 'Achievements')

        tree.column("#0", width=150, minwidth=150)
        tree.column("Creativity Score", anchor=tk.CENTER, width=120)
        tree.column("Engagement Level", anchor=tk.CENTER, width=120)
        tree.column("Achievements", anchor=tk.W, width=200)

        tree.heading("#0", text="Student ID", anchor=tk.W)
        tree.heading("Creativity Score", text="Creativity Score", anchor=tk.CENTER)
        tree.heading("Engagement Level", text="Engagement Level", anchor=tk.CENTER)
        tree.heading("Achievements", text="Achievements", anchor=tk.W)

        for student_id, data in self.class_data.items():
            tree.insert("", tk.END, iid=student_id, text=student_id,
                        values=(data['creativity_score'], data['engagement_level'], ", ".join(data['achievements'])))

        tree.pack(pady=20)

        self.root.mainloop()

if __name__ == "__main__":
    class_data = {
        "student_1": {
            "creativity_score": 75,
            "engagement_level": "Medium",
            "achievements": ["Creative Thinker Badge"]
        },
        "student_2": {
            "creativity_score": 85,
            "engagement_level": "High",
            "achievements": ["Innovator Award", "Team Player Award"]
        },
        # Add more students as needed
    }

    dashboard = TeacherDashboard(class_data)
    dashboard.display_dashboard()
