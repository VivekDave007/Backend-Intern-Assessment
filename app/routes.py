from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Optional
from .database import get_db
from .models import User
from . import schemas, auth

router = APIRouter(prefix="/api", tags=["api"])

@router.post("/auth/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=auth.hash_password(user.password),
        role="user",
        status="active"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/auth/login", response_model=schemas.TokenResponse)
def login(credentials: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not auth.verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    access_token_expires = timedelta(minutes=1440)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    user.last_login = auth.datetime.utcnow()
    db.commit()
    return {"access_token": access_token, "token_type": "bearer", "expires_in": 1440}

@router.get("/users/me", response_model=schemas.UserResponse)
async def get_current_user_profile(current_user: User = Depends(auth.get_current_user)):
    return current_user

@router.put("/users/me", response_model=schemas.UserResponse)
def update_profile(
    user_update: schemas.UserUpdate,
    current_user: User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    if user_update.email and user_update.email != current_user.email:
        existing = db.query(User).filter(User.email == user_update.email).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already in use")
        current_user.email = user_update.email
    if user_update.full_name:
        current_user.full_name = user_update.full_name
    db.commit()
    db.refresh(current_user)
    return current_user

@router.post("/users/change-password")
def change_password(
    pwd_change: schemas.PasswordChangeRequest,
    current_user: User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    if not auth.verify_password(pwd_change.current_password, current_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid current password")
    if pwd_change.new_password != pwd_change.confirm_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passwords do not match")
    current_user.hashed_password = auth.hash_password(pwd_change.new_password)
    db.commit()
    return {"message": "Password changed successfully"}

@router.get("/admin/users", response_model=schemas.UserListResponse)
def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    current_user: User = Depends(auth.get_admin_user),
    db: Session = Depends(get_db)
):
    skip = (page - 1) * limit
    total = db.query(User).count()
    users = db.query(User).offset(skip).limit(limit).all()
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "users": users
    }

@router.get("/admin/users/{user_id}", response_model=schemas.UserResponse)
def get_user(
    user_id: int,
    current_user: User = Depends(auth.get_admin_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put("/admin/users/{user_id}", response_model=schemas.UserResponse)
def update_user(
    user_id: int,
    user_update: schemas.UserUpdate,
    current_user: User = Depends(auth.get_admin_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if user_update.email and user_update.email != user.email:
        existing = db.query(User).filter(User.email == user_update.email).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already in use")
        user.email = user_update.email
    if user_update.full_name:
        user.full_name = user_update.full_name
    if user_update.status:
        user.status = user_update.status
    db.commit()
    db.refresh(user)
    return user

@router.delete("/admin/users/{user_id}")
def delete_user(
    user_id: int,
    current_user: User = Depends(auth.get_admin_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

@router.get("/health")
def health_check():
    return {"status": "healthy"}
