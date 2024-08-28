from crewai import Task
from agents.profiler import profiler

profile_task = Task(
    description=(
        "Compile a detailed personal and professional profile "
        "using the candidate profile ({personal_profile}), candidate resume ({pdf_filepath}), GitHub ({github_url}) URLs "
        "and LinkedIn profile ({linkedin_url}). Utilize tools to extract and "
        "synthesize information from all these sources before forming a "
        "comprehensive profile."
    ),
    expected_output=(
        "A comprehensive profile document that includes skills, "
        "work and project experiences, contributions, interests, "
        "communication style, technical expertise, education, and"
        "ability to learn different technologies."
    ),
    # output_file="candidate_profile.md",
    agent=profiler,
    async_execution=True
)