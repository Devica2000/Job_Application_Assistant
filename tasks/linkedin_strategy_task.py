from crewai import Task
from agents.linkedin_strategist import linkedin_strategist

linkedin_strategy_task = Task(
    description=(
        "Create a unique 'About' section for the candidate's LinkedIn profile using the candidate's profile ({personal_profile}), "
        "resume ({pdf_filepath}), GitHub ({github_url}), and existing LinkedIn profile ({linkedin_url}). "
        "Extract and synthesize relevant information from all these sources. Write the 'About' section in the first person, ensuring it is "
        "tailored to roles in Computer Science, particularly in the fields of ({interested_field}). Do not invent any details; instead, "
        "focus on crafting a compelling narrative that highlights the candidate's strengths and helps them stand out."
    ),
    expected_output=(
        "A tailored 'About' section for the candidate's LinkedIn profile."
    ),
    output_file="linkedin_about.md",
    agent=linkedin_strategist,
    async_execution=True
)