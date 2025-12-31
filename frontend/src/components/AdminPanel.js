import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function AdminPanel({ onLogout }) {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [page, setPage] = useState(1);
  const [totalUsers, setTotalUsers] = useState(0);
  const navigate = useNavigate();
  const token = localStorage.getItem('access_token');
  const limit = 10;

  useEffect(() => {
    fetchUsers();
  }, [page]);

  const fetchUsers = async () => {
    try {
      const response = await fetch(`http://localhost:8000/api/admin/users?page=${page}&limit=${limit}`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      const data = await response.json();
      setUsers(data.users);
      setTotalUsers(data.total);
      setLoading(false);
    } catch (err) {
      setError('Error loading users');
      setLoading(false);
    }
  };

  const handleDeleteUser = async (userId) => {
    if (window.confirm('Are you sure you want to delete this user?')) {
      try {
        const response = await fetch(`http://localhost:8000/api/admin/users/${userId}`, {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });
        if (response.ok) {
          fetchUsers();
          alert('User deleted successfully');
        }
      } catch (err) {
        setError('Error deleting user');
      }
    }
  };

  const handleLogout = () => {
    onLogout();
    navigate('/login');
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  const totalPages = Math.ceil(totalUsers / limit);

  return (
    <div className="admin-panel">
      <div className="navbar">
        <h1>Admin Panel - User Management</h1>
        <button onClick={handleLogout}>Logout</button>
      </div>
      {error && <div className="error-message">{error}</div>}
      <div className="admin-content">
        <div className="users-table-container">
          <h2>All Users</h2>
          <table className="users-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Email</th>
                <th>Name</th>
                <th>Role</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user) => (
                <tr key={user.id}>
                  <td>{user.id}</td>
                  <td>{user.email}</td>
                  <td>{user.full_name}</td>
                  <td>{user.role}</td>
                  <td>{user.status}</td>
                  <td>
                    <button
                      className="delete-btn"
                      onClick={() => handleDeleteUser(user.id)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="pagination">
          <button
            onClick={() => setPage(page - 1)}
            disabled={page === 1}
          >
            Previous
          </button>
          <span>Page {page} of {totalPages}</span>
          <button
            onClick={() => setPage(page + 1)}
            disabled={page === totalPages}
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
}

export default AdminPanel;
