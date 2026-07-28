from app.rag.retriever import get_retriever
from app.schemas.resume import CandidateProfile


def retrieve_candidate_questions(
    profile: CandidateProfile,
    k: int = 5
):

    retriever = get_retriever()

    all_results = []

    # -------------------------
    # 1. Retrieve based on skills
    # -------------------------

    if profile.skills:

        skills_query = f"""
        Generate technical interview questions about these skills:

        {", ".join(profile.skills)}
        """

        skill_results = retriever.invoke(skills_query)

        all_results.extend(skill_results[:k])


    # -------------------------
    # 2. Retrieve based on projects
    # -------------------------

    for project in profile.projects:

        project_query = f"""
        Generate interview questions about this project.

        Project:
        {project}
        """

        project_results = retriever.invoke(project_query)

        all_results.extend(project_results[:k])


    # -------------------------
    # 3. Retrieve based on experience
    # -------------------------

    if profile.experience:

        experience_query = f"""
        Generate interview questions based on this candidate's work experience.

        Experience:
        {profile.experience}
        """

        experience_results = retriever.invoke(experience_query)

        all_results.extend(experience_results[:k])


    return all_results