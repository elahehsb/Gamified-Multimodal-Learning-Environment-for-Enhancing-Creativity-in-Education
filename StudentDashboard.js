import React, { useState, useEffect } from "react";
import axios from "axios";

function StudentDashboard() {
  const [feedback, setFeedback] = useState([]);
  
  useEffect(() => {
    const fetchFeedback = async () => {
      const response = await axios.get(`/feedback/${userId}`);
      setFeedback(response.data.feedback);
    };
    fetchFeedback();
  }, []);

  return (
    <div>
      <h1>Student Dashboard</h1>
      <div className="feedback-section">
        <h2>Feedback</h2>
        <ul>
          {feedback.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default StudentDashboard;
