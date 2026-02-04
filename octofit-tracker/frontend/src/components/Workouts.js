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
    <div className="container mt-4">
      <h2 className="mb-4">💪 Workout Suggestions</h2>
      <div className="row">
        {workouts.length === 0 ? (
          <div className="col-12">
            <div className="alert alert-info">No workout suggestions available.</div>
          </div>
        ) : (
          workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 col-lg-4 mb-3">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{workout.name}</h5>
                  <p className="card-text">
                    <span className={`badge ${getDifficultyBadge(workout.difficulty)} mb-2`}>
                      {workout.difficulty}
                    </span>
                    <br />
                    {workout.description && <span>{workout.description}<br /></span>}
                    {workout.duration && <span><strong>Duration:</strong> {workout.duration} min<br /></span>}
                    {workout.calories_estimate && <span><strong>Calories:</strong> ~{workout.calories_estimate}<br /></span>}
                    {workout.target_muscle_groups && <span><strong>Target:</strong> {workout.target_muscle_groups}</span>}
                  </p>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Workouts;
