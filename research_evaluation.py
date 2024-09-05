# research_evaluation.py

import pandas as pd
from scipy.stats import ttest_ind

class ResearchEvaluation:
    def __init__(self):
        self.quantitative_data = []
        self.qualitative_feedback = []

    def collect_quantitative_data(self, pre_test_scores, post_test_scores):
        self.quantitative_data.append({
            "pre_test": pre_test_scores,
            "post_test": post_test_scores
        })

    def perform_statistical_analysis(self):
        pre_test = [data["pre_test"] for data in self.quantitative_data]
        post_test = [data["post_test"] for data in self.quantitative_data]
        t_stat, p_value = ttest_ind(pre_test, post_test)
        print(f"T-test results: t-statistic = {t_stat}, p-value = {p_value}")
        if p_value < 0.05:
            print("Statistically significant improvement observed.")
        else:
            print("No statistically significant improvement observed.")

    def collect_qualitative_feedback(self, feedback):
        self.qualitative_feedback.append(feedback)

    def analyze_qualitative_feedback(self):
        # Simple frequency analysis of keywords
        feedback_text = " ".join(self.qualitative_feedback)
        keywords = ["engaging", "creative", "challenging", "fun", "difficult"]
        keyword_counts = {keyword: feedback_text.lower().count(keyword) for keyword in keywords}
        print("Qualitative Feedback Analysis:")
        for keyword, count in keyword_counts.items():
            print(f"{keyword.capitalize()}: {count} mentions")

if __name__ == "__main__":
    evaluator = ResearchEvaluation()
    # Simulate data collection
    evaluator.collect_quantitative_data(pre_test_scores=70, post_test_scores=85)
    evaluator.collect_quantitative_data(pre_test_scores=65, post_test_scores=80)
    evaluator.perform_statistical_analysis()

    evaluator.collect_qualitative_feedback("The challenges were very engaging and fun.")
    evaluator.collect_qualitative_feedback("I found the tasks creative but a bit difficult.")
    evaluator.analyze_qualitative_feedback()
