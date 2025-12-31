# React Frontend - Implementation Guide

**Author**: Vivek Dave  
**Theme**: Dark High Contrast (Accessibility First)  
**Status**: Frontend structure created, components to be implemented

---

## Completed Frontend Files

✅ **frontend/package.json** - React dependencies and scripts  
✅ **frontend/src/App.js** - Main app component with routing  
✅ **frontend/src/App.css** - Dark high contrast theme with cyan (#00d9ff) accents  

---

## Remaining React Components to Create

All components should follow the dark high contrast theme from App.css.

### 1. Login Component
**File**: `frontend/src/components/Login.js`
- Login form with email and password fields
- Call `/api/auth/login` endpoint
- Store JWT token in localStorage
- Redirect to dashboard on successful login
- Dark theme with cyan accents

### 2. Register Component
**File**: `frontend/src/components/Register.js`
- Registration form with email, full name, and password
- Call `/api/auth/register` endpoint
- Validate password (min 8 chars)
- Redirect to login on successful registration
- Dark theme styling

### 3. Dashboard Component
**File**: `frontend/src/components/Dashboard.js`
- Display current user profile
- Show edit profile form
- Show change password form
- Call `/api/users/me` for profile data
- Call `PUT /api/users/me` for updates
- Call `POST /api/users/change-password` for password change
- Display user info and profile picture placeholder
- Logout button

### 4. AdminPanel Component
**File**: `frontend/src/components/AdminPanel.js`
- Admin dashboard with user management
- Display users list in table format
- Implement pagination (page, limit)
- Call `GET /api/admin/users?page=X&limit=10`
- Edit user functionality
- Delete user functionality
- Search/filter users
- Dark theme with high contrast table

### 5. API Service
**File**: `frontend/src/services/api.js`
- Axios instance with base URL
- Authentication header with JWT token
- API endpoint functions:
  - `loginUser(email, password)`
  - `registerUser(email, fullName, password)`
  - `getCurrentUser()`
  - `updateProfile(data)`
  - `changePassword(data)`
  - `getUsers(page, limit)`
  - `updateUser(userId, data)`
  - `deleteUser(userId)`

### 6. Other Files
- `frontend/src/index.js` - React entry point
- `frontend/public/index.html` - HTML template
- `frontend/.env.example` - Environment variables template
- `frontend/public/favicon.ico` - Favicon

---

## Dark High Contrast Theme Details

```css
Color Scheme:
- Background: #0a0a0a (Near black)
- Secondary: #1a1a1a (Dark gray)
- Primary: #00d9ff (Bright cyan)
- Accent: #00ffff (Light cyan for hover)
- Text: #ffffff (White)
- Border: 2px solid #00d9ff

Features:
- High contrast text (white on black)
- Bright cyan highlights for all interactive elements
- Glow effects on hover (:hover box-shadow)
- Bold typography
- Clear focus states
- Accessible button sizes
- Responsive design
```

---

## Component Structure

Each component should:
1. Use React Hooks (useState, useEffect)
2. Follow dark high contrast styling
3. Include error handling
4. Show loading states
5. Use Axios for API calls
6. Handle JWT token from localStorage

---

## Installation & Running

```bash
cd frontend
npm install
npm start
```

Access at `http://localhost:3000`

---

## API Integration

Backend API running at: `http://localhost:8000`

All requests should include:
```javascript
headers: {
  'Authorization': `Bearer ${token}`,
  'Content-Type': 'application/json'
}
```

---

## Deployment

Deploy to Vercel:
```bash
npm run build
# Push to GitHub, connect to Vercel
```

---

## Testing

Test accounts:
- Email: `admin@example.com` / Password: `password123` (Admin)
- Email: `user@example.com` / Password: `password123` (User)

---

**Note**: All components must maintain the dark high contrast theme for accessibility compliance.
