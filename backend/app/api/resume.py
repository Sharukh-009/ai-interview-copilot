from fastapi import APIRouter, UploadFile, File
import tempfile
import os

from app.resume.extractor import extract_text
from app.resume.parser import ResumeParser

router = APIRouter()

parser = ResumeParser()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp:

        temp.write(await file.read())
        temp_path = temp.name

    try:
        text = extract_text(temp_path)

        profile = parser.parse(text)

        return profile

    finally:
        os.remove(temp_path)