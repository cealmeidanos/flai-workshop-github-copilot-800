import React, { useState, useEffect } from 'react';

function Coaches() {
  const [coaches, setCoaches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/coaches/`;

  useEffect(() => {
    console.log('Fetching coaches from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Coaches data received:', data);
        const coachesData = data.results || data;
        console.log('Processed coaches data:', coachesData);
        setCoaches(Array.isArray(coachesData) ? coachesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching coaches:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return <div className="text-center"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  return (
    <div className="page-container">
      <div className="container">
        <div className="page-header">
          <h2>👨‍🏫 Fitness Coaches</h2>
        </div>
        
        {coaches.length === 0 ? (
          <div className="alert alert-info">No coaches available.</div>
        ) : (
          <div className="row g-4">
            {coaches.map((coach) => (
              <div key={coach.id} className="col-md-6 col-lg-4">
                <div className="card h-100">
                  <div className="card-body">
                    <h5 className="card-title">{coach.name}</h5>
                    <p className="text-muted mb-3">
                      <strong>📧</strong> {coach.email}
                    </p>
                    <p className="card-text">
                      <span className="badge bg-primary mb-2">{coach.specialization}</span>
                      <br />
                      {coach.bio && <span className="text-muted">{coach.bio}</span>}
                    </p>
                    <hr />
                    <div className="coach-details">
                      <div className="mb-2">
                        <strong>📅 Experience:</strong> {coach.years_experience} years
                      </div>
                      {coach.certifications && coach.certifications.length > 0 && (
                        <div>
                          <strong>🏆 Certifications:</strong>
                          <ul className="mt-2 mb-0">
                            {coach.certifications.map((cert, index) => (
                              <li key={index}>{cert}</li>
                            ))}
                          </ul>
                        </div>
                      )}
                    </div>
                  </div>
                  <div className="card-footer bg-transparent border-top-0">
                    <button className="btn btn-success btn-sm w-100">Contact Coach</button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Coaches;
