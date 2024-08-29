# Job Application Assistant 🖥️📚

**Final Project for Stanford’s Tech16: LLMs for Biz with Python**

## Project Goal

Build an app that simplifies the job application process for job seekers.

## Overview

This app automates job application tasks such as tailoring resumes, crafting personalized LinkedIn messages, researching companies, and generating interview prep materials. It saves job seekers time and effort, allowing them to focus on interview preparation.

## App Inputs

- Job URL
- GitHub URL
- LinkedIn URL
- Personal write-up
- Interested fields

## App Features

- Tailored resume with match score
- Previously asked interview questions (Behavioral & Technical)
- Personalized interview questions with talking points
- Frequently asked LeetCode questions + 4-week study plan
- LinkedIn message templates for outreach

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
2. **Navigate to the project directory:**
   ```bash
   cd Job_Application_Assistant
3. **Create a .env file and add your API keys (refer to .example.env).**
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
5. **Run the app:**
   ```bash
   streamlit run app.py

## Usage
- Enter job, LinkedIn, and GitHub URLs.
- Add a personal write-up and upload your resume (PDF).
- Specify your fields of interest.
- Click "Process Application."
The app provides customized resumes, interview prep materials, and LinkedIn outreach templates.

## Technical Overview:
- **Tools:** DuckDuckGoSearch, ScrapeWebsiteTool, PDFSearchTool, SerperDevTool
- **Agents:** Researcher, Profiler, Resume Strategist, LinkedIn Strategist, Questions Finder, Interview Preparer
- **Crews:** Job Application Crew, LeetCode Crew
