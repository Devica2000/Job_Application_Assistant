# from crewai import Agent
# from crewai_tools import ScrapeWebsiteTool, SerperDevTool, PDFSearchTool
# from langchain.tools import DuckDuckGoSearchRun
# from utils.pdf_tool import PDFReadTool

# search_tool = DuckDuckGoSearchRun() 
# search_tool_serp = SerperDevTool()
# scrape_tool = ScrapeWebsiteTool()
# semantic_search_resume = PDFSearchTool()
# pdf_tool = PDFReadTool()

from crewai import Agent
from utils.tools import scrape_tool, search_tool, pdf_tool, semantic_search_resume

researcher = Agent(
    role="Tech Job Researcher",
    goal="Make sure to do amazing in depth analysis on "
         "job posting to help job applicants get hired for that role.",
    tools=[scrape_tool, search_tool],
    verbose=True,
    backstory=(
        "As a Job Researcher, your prowess in "
        "navigating and extracting critical "
        "information from job postings is unmatched."
        "Your skills help pinpoint the necessary "
        "qualifications and skills sought "
        "by employers, forming the foundation for "
        "effective application tailoring."
    )
)