# Backend Developer Intern Assessment - User Management System

## Project Overview
A full-stack user management application with authentication, role-based access control (RBAC), and comprehensive user lifecycle management. Built with Python FastAPI backend and React frontend.

**Assessment Deadline**: 31 Dec 2025, 11:00 AM IST
**Status**: In Progress

## Technology Stack

### Backend
- **Framework**: FastAPI 0.104+
- **Database**: PostgreSQL / SQLite
- **ORM**: SQLAlchemy 2.0
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt
- **Validation**: Pydantic v2
- **Testing**: Pytest

### Frontend
- **Framework**: React 18+ with Hooks
- **State Management**: React Context / useState
- **Styling**: TailwindCSS
- **Deployment**: Vercel

### Deployment
- **Backend**: Railway / Render / Heroku
- **Database**: Neon PostgreSQL / MongoDB Atlas
- **Frontend**: Vercel / Netlify

## Quick Start

### Backend Setup
```bash
# Clone repository
git clone https://github.com/VivekDave007/Backend-Intern-Assessment.git
cd Backend-Intern-Assessment

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo DATABASE_URL=sqlite:///./test.db > .env
echo JWT_SECRET=your-secret-key >> .env

# Run server
python -m uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`
API Docs at `http://localhost:8000/docs`

## API Endpoints

### Authentication
- `POST /auth/signup` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user

### User Management (Admin)
- `GET /users/` - List all users (pagination)
- `POST /users/{id}/activate` - Activate user
- `POST /users/{id}/deactivate` - Deactivate user

### User Self-Service
- `GET /users/profile/me` - Get own profile
- `PUT /users/profile/me` - Update profile
- `POST /users/password/change` - Change password

## Features Implemented

### Authentication
- [x] User signup with email validation
- [x] User login with credentials
- [x] Password strength validation
- [x] JWT token generation
- [x] Current user retrieval

### User Management
- [x] Admin can view all users (paginated)
- [x] Admin can activate/deactivate users
- [x] Users can view own profile
- [x] Users can update profile (name, email)
- [x] Users can change password
- [x] Last login timestamp tracking

### Security
- [x] Password hashing with bcrypt
- [x] JWT authentication middleware
- [x] Role-based access control (RBAC)
- [x] Input validation on all endpoints
- [x] CORS configuration
- [x] Environment variable management

### Testing
- [x] Unit tests for authentication
- [x] Unit tests for user management
- [x] Unit tests for RBAC
- [x] Integration tests

## Project Structure
```
Backend-Intern-Assessment/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entrypoint
│   ├── config.py            # Configuration & settings
│   ├── database.py          # Database connection
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── auth.py              # Auth utilities (JWT, password hashing)
│   ├── deps.py              # Dependency injection
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py          # Auth routes
│   │   └── users.py         # User management routes
│   └── tests/
│       ├── __init__.py
│       ├── test_auth.py
│       └── test_users.py
├── requirements.txt         # Python dependencies
├── .gitignore
├── .env                    # Environment variables (create locally)
└── README.md
```

## Running Tests
```bash
pytest app/tests/ -v
```

## Environment Variables

Create `.env` file in root:
```
DATABASE_URL=sqlite:///./test.db
JWT_SECRET=your-super-secret-key-change-in-production
CORS_ORIGINS=["http://localhost:3000"]
```

## Deployment

### Deploy to Railway/Render
1. Push code to GitHub
2. Connect repository to Railway/Render
3. Set environment variables
4. Deploy

### Deploy Frontend to Vercel
1. Connect frontend repo to Vercel
2. Set API base URL environment variable
3. Deploy

## Documentation
- API Documentation: `/docs` (Swagger UI)
- ReDoc: `/redoc`

## Submission Checklist
- [ ] Backend code on GitHub
- [ ] Frontend code on GitHub  
- [ ] Backend deployed and accessible
- [ ] Frontend deployed and accessible
- [ ] Database is cloud-hosted
- [ ] README with setup instructions
- [ ] All tests passing
- [ ] Word/PDF report submitted

## Author
Vivek Dave (VivekDave007)

## Internship
Purple Merit Technologies - Backend Developer Intern Assessment
