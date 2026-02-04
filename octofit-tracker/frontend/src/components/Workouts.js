import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Fetching workouts from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts data received:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Processed workouts data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return <div className="text-center"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      'beginner': 'bg-success',
      'intermediate': 'bg-warning',
      'advanced': 'bg-danger'
    };
    return badges[difficulty?.toLowerCase()] || 'bg-secondary';
  };

  return (
    <div className="page-container">
      <div className="container">
        <div className="page-header">
          <h2>💪 Workout Suggestions</h2>
        </div>
        
        {workouts.length === 0 ? (
          <div className="alert alert-info">No workout suggestions available.</div>
        ) : (
          <div className="row g-4">
            {workouts.map((workout) => (
              <div key={workout.id} className="col-md-6 col-lg-4">
                <div className="card h-100">
                  <div className="card-body">
                    <div className="d-flex justify-content-between align-items-start mb-3">
                      <h5 className="card-title mb-0">{workout.title}</h5>
                      <span className={`badge ${getDifficultyBadge(workout.difficulty)} difficulty-badge`}>
                        {workout.difficulty}
                      </span>
                    </div>
                    <p className="card-text text-muted">{workout.description || 'No description available'}</p>
                    <hr />
                    <div className="workout-details">
                      {workout.duration && (
                        <div className="mb-2">
                          <strong>⏱️ Duration:</strong> {workout.duration} min
                        </div>
                      )}
                      {workout.calories_estimate && (
                        <div className="mb-2">
                          <strong>🔥 Calories:</strong> ~{workout.calories_estimate}
                        </div>
                      )}
                      {workout.activity_type && (
                        <div className="mb-2">
                          <strong>🎯 Type:</strong> {workout.activity_type}
                        </div>
                      )}
                      {workout.equipment_needed && workout.equipment_needed.length > 0 && (
                        <div className="mb-2">
                          <strong>🛠️ Equipment:</strong> {workout.equipment_needed.join(', ')}
                        </div>
                      )}
                    </div>
                  </div>
                  <div className="card-footer bg-transparent border-top-0">
                    <button className="btn btn-primary btn-sm w-100">Start Workout</button>
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

export default Workouts;
