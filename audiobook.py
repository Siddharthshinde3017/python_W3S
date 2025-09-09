import pyttsx3
from pypdf import PdfReader

# Use raw string to avoid path issues
reader = PdfReader(r"D:\Code\pytha\full_stak\resume.pdf")

# Get first page text
page = reader.pages[0]
text = page.extract_text()

# Initialize pyttsx3
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
