from crewai import Task
from agents.faq_finder import faq_finder

leetcode_questions_plan = Task(
    description=(
        "Identify and curate the most frequently asked LeetCode questions relevant to the job role specified in the job posting URL ({job_posting_url}). "
        "The curated list should include problems that are commonly encountered in interviews for this role. Additionally, create a personalized 4-week "
        "practice plan for the candidate to solve these problems, ensuring a balanced approach across different difficulty levels (easy, medium, hard). "
        "The plan should be practical and structured to help the candidate effectively prepare for technical interviews."
    ),
    expected_output=(
        "A list of frequently asked LeetCode questions for the specified job role and a detailed 4-week practice plan to solve these problems."
    ),
    output_file="leetcode_plan.md",
    agent=faq_finder,
    async_execution=True
)