# AI Interview Copilot

An AI-powered interview preparation platform that analyzes a candidate's resume, retrieves relevant interview questions using RAG, generates personalized technical questions, and evaluates candidate answers using Google Gemini.

The goal of the project is to provide a structured, resume-aware interview experience rather than a generic chatbot-style interview.

---

## 🚀 Features

- 📄 **Resume Upload & Parsing**
  - Upload a PDF resume.
  - Extract resume text using `pypdf`.
  - Convert unstructured resume text into a structured candidate profile using Gemini and Pydantic.

- 🎯 **Resume-Based Question Retrieval**
  - Retrieves relevant interview questions based on:
    - Candidate skills
    - Projects
    - Work experience
  - Uses semantic similarity search with Gemini embeddings and FAISS.

- 🤖 **AI-Powered Question Generation**
  - Generates personalized technical interview questions using the candidate's profile and retrieved questions.
  - Generates exactly 5 questions for each interview session.
  - Questions are grounded in the candidate's actual resume information.

- 📝 **Answer Evaluation**
  - Evaluates each candidate answer using Google Gemini.
  - Provides:
    - Score out of 10
    - Feedback
    - Strengths
    - Weaknesses

- 📊 **Interview Results**
  - Calculates the candidate's average score.
  - Displays individual question evaluations.
  - Provides an overall interview summary.

- 🔄 **LangGraph Workflow**
  - Uses LangGraph to orchestrate the question retrieval and generation workflow.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │     React Frontend  │
                    └──────────┬──────────┘
                               │
                         Upload Resume
                               │
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI API     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    PDF Extraction   │
                    │       pypdf         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Resume Parser     │
                    │ Gemini + Pydantic   │
                    └──────────┬──────────┘
                               │
                        Candidate Profile
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Candidate RAG     │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       Gemini Embeddings                    FAISS
                │                             │
                └──────────────┬──────────────┘
                               │
                      Relevant Questions
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Question Generator│
                    │       Gemini        │
                    └──────────┬──────────┘
                               │
                     Personalized Questions
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Interview Session │
                    └──────────┬──────────┘
                               │
                         Candidate Answer
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Answer Evaluator  │
                    │       Gemini        │
                    └──────────┬──────────┘
                               │
                    Score + Feedback + Analysis
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Final Interview   │
                    │       Report        │
                    └─────────────────────┘
