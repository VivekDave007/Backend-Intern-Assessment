# Backend Intern Assessment - Setup & Deployment Guide

## Project: User Management System
**Author**: Vivek Dave  
**Organization**: Purple Merit Technologies  
**Deadline**: 31 December 2025, 11:00 AM IST  
**Repository**: https://github.com/VivekDave007/Backend-Intern-Assessment

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Local Setup](#local-setup)
4. [Running Tests](#running-tests)
5. [API Documentation](#api-documentation)
6. [Deployment Instructions](#deployment-instructions)
7. [Troubleshooting](#troubleshooting)

---

## Project Overview

A complete **User Management System** backend built with **Python FastAPI**, featuring:
- ✅ User registration and login with JWT authentication
- ✅ Password hashing with bcrypt
- ✅ Admin user management with pagination
- ✅ User profile management (self-service)
- ✅ Role-based access control (Admin/User)
- ✅ Comprehensive API documentation
- ✅ Unit tests with pytest
- ✅ Production-ready code structure

---

## Tech Stack

### Backend
- **Framework**: FastAPI 0.104.1
- **Server**: Uvicorn
- **Database**: SQLAlchemy ORM with SQLite/PostgreSQL
- **Authentication**: JWT (python-jose) + bcrypt
- **Validation**: Pydantic v2
- **Testing**: pytest
- **API Docs**: Swagger UI, ReDoc

### Dependencies
```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-jose==3.3.0
passlib==1.7.4
bcrypt==4.1.1
pytest==7.4.3
email-validator==2.1.0
python-dotenv==1.0.0
```

---

## Local Setup

### Prerequisites
- Python 3.10 or higher
- pip or poetry
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/VivekDave007/Backend-Intern-Assessment.git
cd Backend-Intern-Assessment
```

### Step 2: Create Virtual Environment
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Environment Variables
```bash
cp .env.example .env
# Edit .env file with your configurations
```

**Example .env content:**
```
DATABASE_URL=sqlite:///./test.db
JWT_SECRET=your-super-secret-key-min-32-chars-long
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]
```

### Step 5: Initialize Database
```bash
python -c "from app.database import init_db; init_db()"
```

### Step 6: Run Development Server
```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:
- **API Base**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_main.py -v
```

### Run with Coverage
```bash
pytest tests/ --cov=app --cov-report=html
```

### Test Results
Tests cover:
- ✅ Health check endpoint
- ✅ User registration
- ✅ Duplicate email prevention
- ✅ Login functionality
- ✅ JWT token validation

---

## API Documentation

### Authentication Endpoints

**Register User**
```bash
POST /api/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "full_name": "User Name",
  "password": "SecurePassword123"
}
```

**Login**
```bash
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePassword123"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "expires_in": 1440
}
```

### User Endpoints

**Get Current User Profile**
```bash
GET /api/users/me
Authorization: Bearer <access_token>
```

**Update Profile**
```bash
PUT /api/users/me
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "email": "newemail@example.com",
  "full_name": "New Name"
}
```

**Change Password**
```bash
POST /api/users/change-password
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "current_password": "OldPassword123",
  "new_password": "NewPassword123",
  "confirm_password": "NewPassword123"
}
```

### Admin Endpoints

**List All Users (Paginated)**
```bash
GET /api/admin/users?page=1&limit=10
Authorization: Bearer <admin_token>
```

**Get User by ID**
```bash
GET /api/admin/users/{user_id}
Authorization: Bearer <admin_token>
```

**Update User (Admin)**
```bash
PUT /api/admin/users/{user_id}
Authorization: Bearer <admin_token>
Content-Type: application/json

{
  "email": "newemail@example.com",
  "full_name": "New Name",
  "status": "active"
}
```

**Delete User**
```bash
DELETE /api/admin/users/{user_id}
Authorization: Bearer <admin_token>
```

---

## Deployment Instructions

### Deploy to Railway

1. **Create Railway Account**
   - Sign up at https://railway.app

2. **Connect GitHub Repository**
   - Link your GitHub account
   - Select Backend-Intern-Assessment repository

3. **Configure Environment**
   - Add variables in Railway dashboard:
     - `DATABASE_URL` (PostgreSQL connection string)
     - `JWT_SECRET` (strong secret key)
     - `JWT_ALGORITHM` (HS256)

4. **Set Start Command**
   ```
   python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

5. **Deploy**
   - Railway automatically deploys on push to main branch

### Deploy to Render

1. **Create Render Account**
   - Sign up at https://render.com

2. **Create Web Service**
   - Connect GitHub repository
   - Select Backend-Intern-Assessment

3. **Configure**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**: Add DATABASE_URL, JWT_SECRET, etc.

4. **Deploy**
   - Click Deploy
   - Wait for build to complete

---

## Project Structure

```
Backend-Intern-Assessment/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application
│   ├── config.py               # Configuration settings
│   ├── database.py             # Database connection
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic schemas
│   ├── auth.py                 # JWT authentication
│   └── routes.py               # API endpoints
├── tests/
│   ├── __init__.py
│   └── test_main.py            # Unit tests
├── .env.example                # Environment template
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── API_DOCUMENTATION.md        # API reference
└── SETUP_AND_DEPLOYMENT_GUIDE.md  # This file
```

---

## Security Features

- ✅ JWT token-based authentication
- ✅ Bcrypt password hashing
- ✅ Role-based access control
- ✅ CORS middleware configuration
- ✅ Environment variable protection
- ✅ SQL injection prevention (ORM)
- ✅ HTTPBearer security scheme

---

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution**: Make sure virtual environment is activated and dependencies are installed
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: Database Connection Error
**Solution**: Check DATABASE_URL in .env file
```bash
# For SQLite
DATABASE_URL=sqlite:///./test.db

# For PostgreSQL
DATABASE_URL=postgresql://user:password@localhost/database_name
```

### Issue: JWT Authentication Failed
**Solution**: Ensure JWT_SECRET is set and is at least 32 characters
```bash
echo $JWT_SECRET  # Check if variable is set
```

### Issue: Port Already in Use
**Solution**: Use a different port
```bash
python -m uvicorn app.main:app --reload --port 8001
```

---

## Additional Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com
- **SQLAlchemy Documentation**: https://docs.sqlalchemy.org
- **JWT Documentation**: https://pyjwt.readthedocs.io
- **Pytest Documentation**: https://docs.pytest.org

---

## Support

For issues or questions, please refer to:
- README.md - Project overview
- API_DOCUMENTATION.md - Detailed API reference
- GitHub Issues - Report bugs and features

---

**Last Updated**: December 31, 2025  
**Version**: 1.0.0  
**Status**: Complete & Ready for Deployment
