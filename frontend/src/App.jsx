import { useState } from "react";
import ResumeUpload from "./components/ResumeUpload";
import Interview from "./pages/Interview";
import "./App.css";

function App() {
  const [profile, setProfile] = useState(null);
  const [interviewStarted, setInterviewStarted] =
    useState(false);

  const handleUploadSuccess = (candidateProfile) => {
    console.log(
      "Profile received:",
      candidateProfile
    );

    setProfile(candidateProfile);
  };

  if (!profile) {
    return (
      <ResumeUpload
        onUploadSuccess={handleUploadSuccess}
      />
    );
  }

  if (!interviewStarted) {
    return (
      <div className="profile-page">

        <header className="profile-header">
          <div>
            <h1>
              AI Interview Copilot
            </h1>

            <p>
              Your Resume Profile
            </p>
          </div>

          <button
            className="start-button"
            onClick={() =>
              setInterviewStarted(true)
            }
          >
            Start Interview →
          </button>
        </header>

        <main className="profile-container">

          {/* Personal Information */}

          <section className="profile-card personal-card">

            <div className="avatar">
              {profile.name
                ?.charAt(0)
                ?.toUpperCase()}
            </div>

            <div>
              <h2>
                {profile.name}
              </h2>

              <p>
                {profile.email}
              </p>
            </div>

          </section>


          {/* Skills */}

          <section className="profile-card">

            <h2>Skills</h2>

            <div className="skills-container">

              {profile.skills?.map(
                (skill, index) => (
                  <span
                    className="skill-tag"
                    key={index}
                  >
                    {skill}
                  </span>
                )
              )}

            </div>

          </section>


          {/* Projects */}

          <section className="profile-card">

            <h2>Projects</h2>

            <div className="project-grid">

              {profile.projects?.map(
                (project, index) => (

                  <div
                    className="project-card"
                    key={index}
                  >

                    <h3>
                      {project.name}
                    </h3>

                    <p>
                      {project.description}
                    </p>

                    <div className="tech-list">

                      {project.technologies?.map(
                        (tech, techIndex) => (

                          <span
                            key={techIndex}
                          >
                            {tech}
                          </span>

                        )
                      )}

                    </div>

                  </div>

                )
              )}

            </div>

          </section>


          {/* Experience */}

          <section className="profile-card">

            <h2>Experience</h2>

            {profile.experience?.map(
              (experience, index) => (

                <div
                  className="experience-item"
                  key={index}
                >

                  <div>
                    <h3>
                      {experience.role}
                    </h3>

                    <p>
                      {experience.company}
                    </p>
                  </div>

                  <div className="experience-right">

                    <span>
                      {experience.duration}
                    </span>

                    <p>
                      {experience.technologies?.join(
                        " • "
                      )}
                    </p>

                  </div>

                </div>

              )
            )}

          </section>


          {/* Education */}

          <section className="profile-card">

            <h2>Education</h2>

            {profile.education?.map(
              (education, index) => (

                <div
                  className="education-item"
                  key={index}
                >

                  <h3>
                    {education.degree}
                  </h3>

                  <p>
                    {education.college}
                  </p>

                  <span>
                    {education.year}
                  </span>

                </div>

              )
            )}

          </section>


          {/* Certifications */}

          <section className="profile-card">

            <h2>Certifications</h2>

            {profile.certifications?.length > 0 ? (

              <ul className="certification-list">

                {profile.certifications.map(
                  (certification, index) => (

                    <li key={index}>
                      {certification}
                    </li>

                  )
                )}

              </ul>

            ) : (

              <p className="empty-text">
                No certifications listed.
              </p>

            )}

          </section>

        </main>

      </div>
    );
  }

  return (
    <Interview
      profile={profile}
    />
  );
}

export default App;