import ResumeUpload from "../components/ResumeUpload";

function Home({ onUploadSuccess }) {
  return (
    <div>
      <ResumeUpload
        onUploadSuccess={onUploadSuccess}
      />
    </div>
  );
}

export default Home;