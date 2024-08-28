from crewai_tools import BaseTool
import PyPDF2

class PDFReadTool(BaseTool):
    name: str = "PDF Reader"
    description: str = "A tool that reads the content of a PDF file. Provide the file path as an argument."

    def _run(self, file_path: str) -> str:
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            return text
        except Exception as e:
            return f"An error occurred while reading the PDF: {str(e)}"