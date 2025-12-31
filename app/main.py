from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Backend Developer Intern Assessment", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    confirm_password: str


class LoginRequest(BaseModel):
        email: str
        password: str
class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    status: str
    role: str

@app.get("/")
async def root():
    return {"message": "Backend API", "status": "running", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/api/auth/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    if user.password != user.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match"
        )
    return {
        "id": 1,
        "email": user.email,
        "full_name": user.full_name,
        "status": "active",
        "role": "user"
    }

@app.post("/api/auth/login")
async def login(user: LoginRequest):    return {"access_token": "token", "token_type": "bearer", "expires_in": 1440}
