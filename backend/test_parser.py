from app.resume.extractor import extract_text
from app.resume.parser import ResumeParser

text = extract_text("resume.pdf")

parser = ResumeParser()

profile = parser.parse(text)

print(profile)