from crewai_tools import ScrapeWebsiteTool, SerperDevTool, PDFSearchTool
from langchain.tools import DuckDuckGoSearchRun
from utils.pdf_tool import PDFReadTool

search_tool = DuckDuckGoSearchRun() 
search_tool_serp = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
semantic_search_resume = PDFSearchTool()
pdf_tool = PDFReadTool()

__all__ = ['search_tool', 'search_tool_serp', 'scrape_tool', 'semantic_search_resume', 'pdf_tool']