from app.schemas.resume import CandidateProfile
from app.services.llm import llm


class ResumeParser:

    def __init__(self):
        self.structured_llm = llm.with_structured_output(CandidateProfile)

    def parse(self, resume_text: str) -> CandidateProfile:

        prompt = f"""
You are an expert resume parser.

Extract the candidate information from the resume.

Rules:
- Return every skill separately.
- Extract all projects.
- Extract technologies used in each project.
- Extract education.
- Extract work experience.
- Extract certifications.
- If something is missing, return an empty list.
- Do not invent information.

Resume:

{resume_text}
"""

        profile = self.structured_llm.invoke(prompt)

        return profile