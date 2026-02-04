import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Fetching leaderboard from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard data received:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Processed leaderboard data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return <div className="text-center"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  const getMedalEmoji = (rank) => {
    if (rank === 1) return '🥇';
    if (rank === 2) return '🥈';
    if (rank === 3) return '🥉';
    return `#${rank}`;
  };

  return (
    <div className="page-container">
      <div className="container">
        <div className="page-header">
          <h2>🏅 Leaderboard</h2>
        </div>
        
        <div className="card">
          <div className="card-body">
            {leaderboard.length === 0 ? (
              <div className="alert alert-info">No leaderboard data available.</div>
            ) : (
              <div className="table-responsive">
                <table className="table table-hover align-middle">
                  <thead>
                    <tr>
                      <th>Rank</th>
                      <th>User/Team</th>
                      <th>Total Points</th>
                      <th>Activities</th>
                      <th>Last Update</th>
                    </tr>
                  </thead>
                  <tbody>
                    {leaderboard.map((entry, index) => (
                      <tr key={entry.id}>
                        <td><span className="medal-rank">{getMedalEmoji(entry.rank || index + 1)}</span></td>
                        <td><strong>{entry.user_name || entry.team_name || entry.user || entry.team}</strong></td>
                        <td><span className="badge bg-primary fs-6">{entry.total_points}</span></td>
                        <td><span className="badge bg-info">{entry.total_activities || 0}</span></td>
                        <td>{entry.last_activity_date ? new Date(entry.last_activity_date).toLocaleDateString() : <span className="text-muted">N/A</span>}</td>
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

export default Leaderboard;
