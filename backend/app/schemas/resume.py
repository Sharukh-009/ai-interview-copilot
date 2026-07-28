from pydantic import BaseModel, EmailStr


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str]


class Experience(BaseModel):
    company: str
    role: str
    duration: str
    technologies: list[str]


class Education(BaseModel):
    degree: str
    college: str
    year: str


class CandidateProfile(BaseModel):
    name: str
    email: EmailStr

    skills: list[str]

    projects: list[Project]

    experience: list[Experience]

    education: list[Education]

    certifications: list[str]