import { useEffect, useState } from "react";
import axios from "axios";
import "./Interview.css";

function Interview({ profile }) {
  const [sessionId, setSessionId] = useState(null);

  const [question, setQuestion] = useState("");
  const [questionNumber, setQuestionNumber] = useState(1);

  const [nextQuestion, setNextQuestion] = useState("");
  const [nextQuestionNumber, setNextQuestionNumber] = useState(1);

  const [answer, setAnswer] = useState("");
  const [submittedAnswer, setSubmittedAnswer] = useState("");

  const [evaluation, setEvaluation] = useState(null);
  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  const [interviewComplete, setInterviewComplete] =
    useState(false);


  // ----------------------------------------
  // START INTERVIEW
  // ----------------------------------------

  useEffect(() => {
    startInterview();
  }, []);


  const startInterview = async () => {
    try {
      setLoading(true);

      const response = await axios.post(
        "http://localhost:8000/interview/start",
        profile
      );

      setSessionId(
        response.data.session_id
      );

      setQuestion(
        response.data.question
      );

      setQuestionNumber(
        response.data.question_number
      );

    } catch (error) {
      console.error(
        "Error starting interview:",
        error
      );

      alert(
        "Failed to start interview"
      );

    } finally {
      setLoading(false);
    }
  };


  // ----------------------------------------
  // SUBMIT ANSWER
  // ----------------------------------------

  const submitAnswer = async () => {

    if (!answer.trim()) {
      alert(
        "Please enter your answer before submitting."
      );
      return;
    }

    try {
      setSubmitting(true);

      // Save exactly what the candidate submitted
      setSubmittedAnswer(answer);

      const response = await axios.post(
        `http://localhost:8000/interview/${sessionId}/answer`,
        {
          answer: answer
        }
      );

      const data = response.data;

      // Save evaluation
      setEvaluation(
        data.evaluation
      );


      // ----------------------------------------
      // INTERVIEW COMPLETE
      // ----------------------------------------

      if (data.interview_complete) {

        setInterviewComplete(true);

        setResult(
          data.result
        );

        return;
      }


      // ----------------------------------------
      // SAVE NEXT QUESTION
      // ----------------------------------------

      setNextQuestion(
        data.next_question
      );

      setNextQuestionNumber(
        data.question_number
      );

      setAnswer("");

    } catch (error) {

      console.error(
        "Error submitting answer:",
        error
      );

      alert(
        "Failed to submit answer."
      );

    } finally {
      setSubmitting(false);
    }
  };


  // ----------------------------------------
  // NEXT QUESTION
  // ----------------------------------------

  const goToNextQuestion = () => {

    setQuestion(
      nextQuestion
    );

    setQuestionNumber(
      nextQuestionNumber
    );

    setEvaluation(null);

    setSubmittedAnswer("");

    setAnswer("");
  };


  // ----------------------------------------
  // LOADING
  // ----------------------------------------

  if (loading) {

    return (
      <div className="interview-page">

        <div className="loading-card">

          <div className="loader"></div>

          <h2>
            Preparing Your Interview
          </h2>

          <p>
            Generating personalized questions
            based on your resume...
          </p>

        </div>

      </div>
    );
  }


  // ----------------------------------------
  // FINAL RESULT
  // ----------------------------------------

//   if (interviewComplete) {

//     return (
//       <div className="interview-page">

//         <div className="result-container">

//           <div className="result-header">

//             <div className="success-icon">
//               ✓
//             </div>

//             <h1>
//               Interview Completed
//             </h1>

//             <p>
//               Great job! Here's your
//               interview performance.
//             </p>

//           </div>


//           {result && (

//             <>

//               <div className="score-card">

//                 <div>
//                   <span>
//                     Average Score
//                   </span>

//                   <strong>
//                     {Number(
//                       result.average_score
//                     ).toFixed(1)}
//                     <small>
//                       /10
//                     </small>
//                   </strong>
//                 </div>


//                 <div>
//                   <span>
//                     Questions
//                   </span>

//                   <strong>
//                     {result.answered_questions}
//                     <small>
//                       /{result.total_questions}
//                     </small>
//                   </strong>
//                 </div>

//               </div>


//               <h2 className="section-title">
//                 Detailed Performance
//               </h2>


//               <div className="results-list">

//                 {result.evaluations?.map(
//                   (item, index) => (

//                     <div
//                       className="result-item"
//                       key={index}
//                     >

//                       <div className="result-question">

//                         <span>
//                           Question {index + 1}
//                         </span>

//                         <p>
//                           {item.question}
//                         </p>

//                       </div>


//                       <div className="result-answer">

//                         <h4>
//                           Your Answer
//                         </h4>

//                         <p>
//                           {item.answer}
//                         </p>

//                       </div>


//                       <div className="result-evaluation">

//                         <h4>
//                           Evaluation
//                         </h4>

//                         <pre>
//                           {JSON.stringify(
//                             item.evaluation,
//                             null,
//                             2
//                           )}
//                         </pre>

//                       </div>

//                     </div>

//                   )
//                 )}

//               </div>

//             </>
//           )}

//         </div>

//       </div>
//     );
//   }
if (interviewComplete) {
  return (
    <div className="interview-page">

      <div className="result-container">

        {/* Header */}
        <div className="result-header">

          <div className="success-icon">
            ✓
          </div>

          <p className="eyebrow">
            INTERVIEW COMPLETE
          </p>

          <h1>
            Your Interview Results
          </h1>

          <p>
            Here's a detailed breakdown of your
            technical interview performance.
          </p>

        </div>


        {result && (
          <>

            {/* Summary Cards */}
            <div className="score-card">

              <div>
                <span>
                  Overall Score
                </span>

                <strong>
                  {Number(
                    result.average_score || 0
                  ).toFixed(1)}

                  <small>
                    /10
                  </small>
                </strong>
              </div>


              <div>
                <span>
                  Questions Answered
                </span>

                <strong>
                  {result.answered_questions}

                  <small>
                    /{result.total_questions}
                  </small>
                </strong>
              </div>

            </div>


            {/* Performance */}
            <h2 className="section-title">
              Question-by-Question Performance
            </h2>


            <div className="results-list">

              {result.evaluations?.map(
                (item, index) => {

                  const evaluation =
                    typeof item.evaluation === "object"
                      ? item.evaluation
                      : null;

                  return (

                    <div
                      className="result-item"
                      key={index}
                    >

                      {/* Question Header */}
                      <div className="result-question">

                        <span>
                          QUESTION {index + 1}
                        </span>

                        <p>
                          {item.question}
                        </p>

                      </div>


                      {/* Candidate Answer */}
                      <div className="result-answer">

                        <h4>
                          Your Answer
                        </h4>

                        <p>
                          {item.answer}
                        </p>

                      </div>


                      {/* AI Evaluation */}
                      {evaluation ? (

                        <div className="result-evaluation">

                          <div className="evaluation-header">

                            <h4>
                              AI Evaluation
                            </h4>

                            <div className="result-score">

                              {evaluation.score}

                              <span>
                                /10
                              </span>

                            </div>

                          </div>


                          <div className="result-feedback">

                            <div>

                              <h5>
                                Feedback
                              </h5>

                              <p>
                                {evaluation.feedback}
                              </p>

                            </div>


                            <div>

                              <h5>
                                Strengths
                              </h5>

                              <p>
                                {evaluation.strengths}
                              </p>

                            </div>


                            <div>

                              <h5>
                                Areas to Improve
                              </h5>

                              <p>
                                {evaluation.weaknesses}
                              </p>

                            </div>

                          </div>

                        </div>

                      ) : (

                        <div className="result-evaluation">

                          <h4>
                            Evaluation
                          </h4>

                          <p>
                            {item.evaluation}
                          </p>

                        </div>

                      )}

                    </div>

                  );

                }
              )}

            </div>

          </>
        )}

      </div>

    </div>
  );
}

  // ----------------------------------------
  // EVALUATION SCREEN
  // ----------------------------------------

  if (evaluation) {

    return (
      <div className="interview-page">

        <div className="interview-container">

          <div className="progress">
            Question {questionNumber}
          </div>


          <div className="question-card">

            <h2>
              {question}
            </h2>

          </div>


          {/* Candidate's Answer */}

          <div className="answer-card">

            <div className="card-label">
              Your Answer
            </div>

            <p>
              {submittedAnswer}
            </p>

          </div>


          {/* Evaluation */}

          <div className="evaluation-card">

            <div className="card-label">
              AI Evaluation
            </div>


            {typeof evaluation === "object" ? (

              <>

                <div className="score-display">

                  <span>
                    Score
                  </span>

                  <strong>
                    {evaluation.score}
                    <small>
                      /10
                    </small>
                  </strong>

                </div>


                <div className="feedback">

                  <div>
                    <h4>
                      Feedback
                    </h4>

                    <p>
                      {evaluation.feedback}
                    </p>
                  </div>


                  <div>
                    <h4>
                      Strengths
                    </h4>

                    <p>
                      {evaluation.strengths}
                    </p>
                  </div>


                  <div>
                    <h4>
                      Areas to Improve
                    </h4>

                    <p>
                      {evaluation.weaknesses}
                    </p>
                  </div>

                </div>

              </>

            ) : (

              <p>
                {evaluation}
              </p>

            )}

          </div>


          <button
            className="primary-button"
            onClick={
              goToNextQuestion
            }
          >
            Next Question →
          </button>

        </div>

      </div>
    );
  }


  // ----------------------------------------
  // QUESTION SCREEN
  // ----------------------------------------

  return (
    <div className="interview-page">

      <div className="interview-container">


        <div className="interview-header">

          <div>

            <p className="eyebrow">
              AI INTERVIEW COPILOT
            </p>

            <h1>
              Personalized Technical Interview
            </h1>

          </div>

          <div className="question-counter">
            Question {questionNumber}
          </div>

        </div>


        <div className="question-card">

          <span className="card-label">
            Interview Question
          </span>

          <h2>
            {question}
          </h2>

        </div>


        <div className="answer-input-card">

          <label>
            Your Answer
          </label>

          <textarea
            value={answer}
            onChange={(e) =>
              setAnswer(e.target.value)
            }
            placeholder="Explain your approach, reasoning, and relevant experience..."
            rows={9}
          />


          <div className="answer-footer">

            <span>
              Take your time and answer
              as if you're in a real interview.
            </span>


            <button
              className="primary-button"
              onClick={
                submitAnswer
              }
              disabled={submitting}
            >

              {submitting
                ? "Evaluating..."
                : "Submit Answer →"}

            </button>

          </div>

        </div>

      </div>

    </div>
  );
}

export default Interview;