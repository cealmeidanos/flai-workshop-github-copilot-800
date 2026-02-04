import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Fetching activities from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities data received:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        console.log('Processed activities data:', activitiesData);
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching activities:', error);
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
          <h2>🏃 Activities</h2>
        </div>
        
        <div className="card">
          <div className="card-body">
            {activities.length === 0 ? (
              <div className="alert alert-info">No activities found.</div>
            ) : (
              <div className="table-responsive">
                <table className="table table-hover align-middle">
                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>User</th>
                      <th>Type</th>
                      <th>Duration</th>
                      <th>Distance</th>
                      <th>Calories</th>
                      <th>Date</th>
                    </tr>
                  </thead>
                  <tbody>
                    {activities.map((activity) => (
                      <tr key={activity.id}>
                        <td><span className="badge bg-secondary">{activity.id}</span></td>
                        <td><strong>{activity.user_name || activity.user}</strong></td>
                        <td><span className="badge bg-info">{activity.activity_type}</span></td>
                        <td>{activity.duration} min</td>
                        <td>{activity.distance ? `${activity.distance} km` : <span className="text-muted">N/A</span>}</td>
                        <td>{activity.calories} cal</td>
                        <td>{activity.date ? new Date(activity.date).toLocaleDateString() : <span className="text-muted">N/A</span>}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Activities;
