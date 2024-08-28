from crewai import Task
from agents.linkedin_strategist import linkedin_strategist
from tasks.profile_task import profile_task
from tasks.research_task import research_task

linkedin_message_task = Task(
    description=(
        "Draft a LinkedIn cold outreach message template for the candidate to use when reaching out to potential employers. "
        "The message should politely request referrals or coffee chats and be tailored to employees at a company of interest. "
        "Use the candidate's profile ({personal_profile}), resume ({pdf_filepath}), GitHub ({github_url}), and LinkedIn profile ({linkedin_url}) "
        "to create this message. Write in the first person, reflecting the candidate's communication style and personality. Ensure the message is "
        "concise yet effective, increasing the likelihood of a positive response. Tailor the content specifically to the job role ({job_posting_url}) "
        "and the target company's employees."
    ),
    expected_output=(
        "A customized LinkedIn cold outreach message for the candidate's specified job role and target company."
    ),
    output_file="linkedin_message.md",
    agent=linkedin_strategist,
    context=[research_task, profile_task]
)
