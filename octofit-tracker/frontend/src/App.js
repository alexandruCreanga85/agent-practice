
import React from 'react';

function App() {
  return (
    <div>
      {/* Bootstrap Navigation */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">OctoFit Tracker</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#activities">Activities</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#teams">Teams</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#leaderboard">Leaderboard</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-md-8">
            <div className="card shadow">
              <div className="card-body">
                <h1 className="card-title display-4 text-center mb-4">Welcome to OctoFit Tracker</h1>
                <p className="card-text text-center">Track your fitness activities, join teams, and climb the leaderboard!</p>
                <div className="d-flex justify-content-center mt-4">
                  <a href="#activities" className="btn btn-primary mx-2">View Activities</a>
                  <a href="#teams" className="btn btn-outline-primary mx-2">View Teams</a>
                  <a href="#leaderboard" className="btn btn-success mx-2">Leaderboard</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
