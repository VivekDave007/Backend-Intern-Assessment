# User Management System - API Documentation

## Overview
Complete user management system with JWT authentication, admin functionality, and comprehensive API endpoints.

## Base URL
```
http://localhost:8000
http://localhost:8000/api
```

## Authentication
All protected endpoints require JWT Bearer token in Authorization header:
```
Authorization: Bearer <access_token>
```

## API Endpoints

### Authentication

#### Register User
- **POST** `/api/auth/register`
- **Body**: `{"email": "user@example.com", "full_name": "User", "password": "pass123"}`
- **Response**: 201 Created - User object

#### Login
- **POST** `/api/auth/login`
- **Body**: `{"email": "user@example.com", "password": "pass123"}`
- **Response**: 200 OK - `{"access_token": "...", "token_type": "bearer", "expires_in": 1440}`

### User Profile

#### Get Current User
- **GET** `/api/users/me`
- **Auth**: Required
- **Response**: 200 OK - User object

#### Update Profile
- **PUT** `/api/users/me`
- **Auth**: Required
- **Body**: `{"email": "...", "full_name": "..."}`
- **Response**: 200 OK - Updated user object

#### Change Password
- **POST** `/api/users/change-password`
- **Auth**: Required
- **Body**: `{"current_password": "...", "new_password": "...", "confirm_password": "..."}`
- **Response**: 200 OK

### Admin Endpoints

#### List Users (Paginated)
- **GET** `/api/admin/users?page=1&limit=10`
- **Auth**: Admin Required
- **Response**: 200 OK - `{"total": ..., "page": 1, "limit": 10, "users": [...]}`

#### Get User by ID
- **GET** `/api/admin/users/{user_id}`
- **Auth**: Admin Required
- **Response**: 200 OK - User object

#### Update User (Admin)
- **PUT** `/api/admin/users/{user_id}`
- **Auth**: Admin Required
- **Body**: `{"email": "...", "full_name": "...", "status": "active|inactive"}`
- **Response**: 200 OK - Updated user object

#### Delete User
- **DELETE** `/api/admin/users/{user_id}`
- **Auth**: Admin Required
- **Response**: 200 OK - `{"message": "User deleted successfully"}`

### Health & Status

#### Health Check
- **GET** `/health`
- **Auth**: Not Required
- **Response**: 200 OK - `{"status": "healthy", "version": "1.0.0"}`

#### Root Endpoint
- **GET** `/`
- **Auth**: Not Required
- **Response**: 200 OK - `{"message": "...", "docs": "/docs", "redoc": "/redoc"}`

## Database Schema

### Users Table
```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  email VARCHAR UNIQUE NOT NULL,
  hashed_password VARCHAR NOT NULL,
  full_name VARCHAR NOT NULL,
  role ENUM('admin', 'user') DEFAULT 'user',
  status ENUM('active', 'inactive') DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_login TIMESTAMP
);
```

## Tech Stack
- **Framework**: FastAPI
- **Database**: SQLite/PostgreSQL (SQLAlchemy ORM)
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt
- **Validation**: Pydantic
- **Testing**: pytest
- **API Documentation**: Swagger UI, ReDoc

## Error Responses
All errors return appropriate HTTP status codes with descriptive messages.

## Testing
Run tests with: `pytest tests/`
