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

resume_strategist = Agent(
    role="Resume Strategist for early career professionals in the US",
    goal="Find all the best ways to refine and make a "
         "resume stand out in the job market.",
    tools = [scrape_tool, search_tool,
             pdf_tool, semantic_search_resume],
    verbose=True,
    backstory=(
        "With a strategic mind and an eye for detail, you "
        "excel at refining resumes to highlight the most "
        "relevant skills and experiences, ensuring they "
        "resonate perfectly with the job's requirements"
        "without taking away any detail already highlighted"
        "in the resume. With your analytical capabilities"
        "you calculate the percentage match between the "
        "original resume and the job posting and also the"
        "refined resume and the job posting."
    )
)