from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    admin = "admin"
    user = "user"

class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"

class UserBase(BaseModel):
    email: str
    full_name: str

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    status: Optional[UserStatus] = None

class UserChangePassword(BaseModel):
    old_password: str
    new_password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    role: UserRole
    status: UserStatus
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True

class UserListResponse(BaseModel):
    total: int
    page: int
    limit: int
    users: list[UserResponse]

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class LoginRequest(BaseModel):
    email: str
    password: str

class PasswordChangeRequest(BaseModel):
    current_password: str
    new_password: str = Field(..., min_length=8)
    confirm_password: str

class TokenData(BaseModel):
    user_id: int
