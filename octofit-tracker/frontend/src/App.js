import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Teams from './components/Teams';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';

function Home() {
  return (
    <div className="page-container">
      <div className="container">
        <div className="home-hero rounded">
          <h1 className="display-3">🏋️ OctoFit Tracker</h1>
          <p className="lead">Track your fitness journey and compete with your team!</p>
        </div>
        
        <div className="row g-4">
          <div className="col-md-4">
            <div className="card text-center">
              <div className="card-body">
                <h3 className="card-title">👥 Users</h3>
                <p className="card-text">Manage and view user profiles</p>
                <Link to="/users" className="btn btn-primary">View Users</Link>
              </div>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card text-center">
              <div className="card-body">
                <h3 className="card-title">🏆 Teams</h3>
                <p className="card-text">Explore team collaborations</p>
                <Link to="/teams" className="btn btn-primary">View Teams</Link>
              </div>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card text-center">
              <div className="card-body">
                <h3 className="card-title">🏃 Activities</h3>
                <p className="card-text">Track fitness activities</p>
                <Link to="/activities" className="btn btn-primary">View Activities</Link>
              </div>
            </div>
          </div>
          <div className="col-md-6">
            <div className="card text-center">
              <div className="card-body">
                <h3 className="card-title">🏅 Leaderboard</h3>
                <p className="card-text">Check competitive rankings</p>
                <Link to="/leaderboard" className="btn btn-success">View Leaderboard</Link>
              </div>
            </div>
          </div>
          <div className="col-md-6">
            <div className="card text-center">
              <div className="card-body">
                <h3 className="card-title">💪 Workouts</h3>
                <p className="card-text">Get personalized workout suggestions</p>
                <Link to="/workouts" className="btn btn-success">View Workouts</Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  const API_BASE = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`;
  console.log('OctoFit Tracker - API Base URL:', API_BASE);

  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              🏋️ OctoFit Tracker
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/">Home</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
