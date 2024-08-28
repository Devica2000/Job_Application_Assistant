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

profiler = Agent(
    role="Personal Profiler for Engineers",
    goal="Do incredible research on job applicants "
         "to help them stand out in the job market",
    tools = [scrape_tool, search_tool,
             pdf_tool, semantic_search_resume],
    verbose=True,
    backstory=(
        "Equipped with analytical prowess, you dissect "
        "and synthesize information "
        "from diverse sources to craft comprehensive "
        "personal and professional profiles, laying the "
        "groundwork for personalized resume enhancements."
    )
)