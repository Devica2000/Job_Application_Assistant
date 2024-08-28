from crewai import Task
from agents.resume_strategist import resume_strategist
from tasks.profile_task import profile_task
from tasks.research_task import research_task

resume_strategy_task = Task(
    description=(
        "Refine the candidate's resume ({pdf_filepath}) based on the job requirements "
        "from previous tasks. Focus on highlighting relevant skills and experiences that align "
        "with the role, increasing the candidate's chances of being hired. Ensure the resume "
        "effectively reflects the candidate's abilities and matches the job posting without adding "
        "any fabricated information. Update every section to enhance alignment with the job description. "
        "Begin by calculating the match score between the original resume and the job posting, and aim to "
        "improve this score in the revised resume. The final resume should be concise, not exceeding one page."
    ),
    expected_output=(
        "A revised resume tailored to the provided job posting, including both the original and updated match scores."
    ),
    output_file="tailored_resume.md",
    context=[research_task, profile_task],
    agent=resume_strategist
)