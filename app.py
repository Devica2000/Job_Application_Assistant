# app.py

import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from agents import researcher, profiler, resume_strategist, linkedin_strategist, interview_preparer, faq_finder
from tasks import (
    research_task, profile_task, resume_strategy_task, linkedin_strategy_task,
    linkedin_message_task, interview_preparation_task, previously_asked_questions,
    leetcode_questions_plan
)
from utils import PDFReadTool, search_tool, search_tool_serp, scrape_tool, semantic_search_resume
from openai import APIError

# Load environment variables
load_dotenv()

# Set up Streamlit page
st.set_page_config(page_title="Job Application Assistant", page_icon="🚀", layout="wide")
st.title("Job Application Assistant")

# Input fields
job_posting_url = st.text_input("Job Posting URL")
personal_profile = st.text_area("Personal Profile")
github_url = st.text_input("GitHub URL")
linkedin_url = st.text_input("LinkedIn URL")
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type="pdf")
interested_field = st.text_input("Interested Field")

# Set up OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    openai_api_key = st.text_input("Enter your OpenAI API key", type="password")
    if not openai_api_key:
        st.warning("Please enter your OpenAI API key to proceed.")
        st.stop()

# Set environment variables for CrewAI
os.environ['OPENAI_API_KEY'] = openai_api_key
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'

def display_file_content(file_name, subheader):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            st.subheader(subheader)
            st.markdown(f.read())
        return True
    return False

def process_crew_task(crew, inputs, task_name):
    try:
        return crew.kickoff(inputs=inputs)
    except APIError as e:
        st.error(f"Error in {task_name}: {str(e)}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred in {task_name}: {str(e)}")
        return None

if st.button("Process Application"):
    resume_content = None
    if uploaded_resume:
        pdf_tool = PDFReadTool()
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(uploaded_resume.getvalue())
            tmp_file_path = tmp_file.name
        pdf_filepath = pdf_tool._run(tmp_file_path)
        os.unlink(tmp_file_path)  # Remove the temporary file

    job_application_inputs = {
        'job_posting_url': job_posting_url,
        'personal_profile': personal_profile,
        'github_url': github_url,
        'linkedin_url': linkedin_url,
        'pdf_filepath': pdf_filepath,
        'interested_field': interested_field
    }

    job_application_crew = Crew(
        agents=[researcher, profiler, resume_strategist, linkedin_strategist, interview_preparer],
        tasks=[research_task, profile_task, resume_strategy_task, linkedin_message_task, interview_preparation_task],
        verbose=True
    )

    leetcode_crew = Crew(
        agents=[faq_finder],
        tasks=[previously_asked_questions, leetcode_questions_plan],
        verbose=True
    )

    with st.spinner("Processing your application..."):
        result_linkedin = process_crew_task(job_application_crew, job_application_inputs, "Job Application")
        result_leetcode = process_crew_task(leetcode_crew, job_application_inputs, "LeetCode Preparation")

    if result_linkedin or result_leetcode:
        st.success("Processing complete!")

        # Display results
        st.header("Results")

        files_displayed = False
        files_to_display = [
            ("tailored_resume.md", "Tailored Resume"),
            ("interview_preparation.md", "Interview Preparation"),
            ("linkedin_about.md", "LinkedIn About Section"),
            ("linkedin_message.md", "LinkedIn Message"),
            ("faq_questions.md", "Frequently Asked Questions"),
            ("leetcode_plan.md", "LeetCode Plan")
        ]

        for file_name, subheader in files_to_display:
            if display_file_content(file_name, subheader):
                files_displayed = True

        if not files_displayed:
            st.warning("No output files were generated. Displaying raw results.")
            st.subheader("Raw Results")
            if result_linkedin:
                st.write("LinkedIn Crew Results:")
                st.write(result_linkedin)
            if result_leetcode:
                st.write("LeetCode Crew Results:")
                st.write(result_leetcode)
    else:
        st.error("Processing failed. Please try again with different inputs or contact support.")
