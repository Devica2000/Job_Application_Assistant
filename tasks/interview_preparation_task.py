from crewai import Task
from agents.interview_preparer import interview_preparer
from tasks.profile_task import profile_task
from tasks.research_task import research_task

interview_preparation_task = Task(
    description=(
        "Analyze the candidate's resume ({pdf_filepath}) and the job description ({job_posting_url}) to generate tailored interview preparation materials. "
        "Create a set of customized interview questions both behavioral and technical and talking points that align with the candidate's experience and the"
        "specific requirements of the job role. Create questions in the easy, medium, and hard level of difficulty."
        "The questions should be designed to help the candidate highlight their strengths and address relevant aspects of the job. Ensure that the talking points cover "
        "key achievements and skills from the resume that are pertinent to the job role. Provide a comprehensive overview that will help the candidate effectively prepare for the interview."
    ),
    expected_output=(
        "A set of customized interview questions and talking points tailored to the candidate's resume and the job description. "
        "The output should help the candidate address key aspects of the job role and effectively showcase their qualifications during the interview."
    ),
    output_file="interview_preparation.md",
    agent=interview_preparer,
    context=[profile_task, research_task],
    # async_execution=True
)