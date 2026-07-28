import { useState } from "react";
import axios from "axios";
import "./ResumeUpload.css";

function ResumeUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a PDF resume first.");
      return;
    }

    setLoading(true);
    setError("");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://localhost:8000/resume/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log("FULL BACKEND RESPONSE:", response.data);

      const candidateProfile = response.data;

      console.log(
        "CANDIDATE PROFILE:",
        candidateProfile
      );

      onUploadSuccess(candidateProfile);

    } catch (err) {
      console.error(
        "Resume upload failed:",
        err
      );

      setError(
        err.response?.data?.detail ||
        err.message ||
        "Failed to upload resume."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-page">

      <div className="upload-card">

        <div className="upload-icon">
          📄
        </div>

        <h1>
          AI Interview Copilot
        </h1>

        <p className="upload-subtitle">
          Upload your resume and get a
          personalized AI-powered interview.
        </p>

        <div className="upload-box">

          <input
            type="file"
            accept=".pdf"
            id="resume-input"
            onChange={(e) => {
              setFile(e.target.files[0]);
              setError("");
            }}
          />

          <label htmlFor="resume-input">
            {file
              ? file.name
              : "Choose your PDF resume"}
          </label>

        </div>

        {file && (
          <p className="file-selected">
            ✓ Resume selected
          </p>
        )}

        {error && (
          <p className="error-message">
            {error}
          </p>
        )}

        <button
          className="primary-button"
          onClick={handleUpload}
          disabled={loading}
        >
          {loading
            ? "Analyzing Resume..."
            : "Upload & Analyze Resume"}
        </button>

        <p className="upload-info">
          Your resume will be analyzed to
          create personalized interview questions.
        </p>

      </div>

    </div>
  );
}

export default ResumeUpload;