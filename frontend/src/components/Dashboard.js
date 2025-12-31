import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function Dashboard({ onLogout }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [currentPassword, setCurrentPassword] = useState('');
  const navigate = useNavigate();
  const token = localStorage.getItem('access_token');

  useEffect(() => {
    fetchUserProfile();
  }, []);

  const fetchUserProfile = async () => {
    try {
      const response = await fetch('https://backend-intern-assessment-tz83.onrender.com/api/users/me', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      const data = await response.json();
      setUser(data);
      setLoading(false);
    } catch (err) {
      setError('Error loading profile');
      setLoading(false);
    }
  };

  const handleLogout = () => {
    onLogout();
    navigate('/login');
  };

  const handlePasswordChange = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('https://backend-intern-assessment-tz83.onrender.com/api/users/change-password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({
          current_password: currentPassword,
          new_password: newPassword,
          confirm_password: newPassword,
        }),
      });
      if (response.ok) {
        setCurrentPassword('');
        setNewPassword('');
        alert('Password changed successfully');
      } else {
        setError('Failed to change password');
      }
    } catch (err) {
      setError('Error changing password');
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="dashboard">
      <div className="navbar">
        <h1>Dashboard</h1>
        <button onClick={handleLogout}>Logout</button>
      </div>
      {error && <div className="error-message">{error}</div>}
      {user && (
        <div className="dashboard-content">
          <div className="user-info">
            <h2>Profile Information</h2>
            <p><strong>Name:</strong> {user.full_name}</p>
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Role:</strong> {user.role}</p>
            <p><strong>Status:</strong> {user.status}</p>
          </div>
          <div className="change-password">
            <h2>Change Password</h2>
            <form onSubmit={handlePasswordChange}>
              <div className="form-group">
                <label>Current Password:</label>
                <input
                  type="password"
                  value={currentPassword}
                  onChange={(e) => setCurrentPassword(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label>New Password:</label>
                <input
                  type="password"
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  required
                />
              </div>
              <button type="submit">Change Password</button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default Dashboard;
