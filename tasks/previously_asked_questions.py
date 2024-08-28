from crewai import Task
from agents.faq_finder import faq_finder

previously_asked_questions = Task(
    description=(
        "Search the web to find and compile a list of the most frequently asked interview questions for the job role specified in "
        "the provided job posting URL ({job_posting_url}). The list should include both technical and behavioral questions. Ensure "
        "that each question is cited with its source for reference. The goal is to provide a comprehensive set of questions that "
        "candidates might face during interviews for this role. List the questions in decreasing order of their frequency."
    ),
    expected_output=(
        "A list of frequently asked interview questions for the specified job role, including both technical and behavioral questions, "
        "with each question cited with its source."
    ),
    output_file="faq_questions.md",
    agent=faq_finder,
    async_execution=True
)