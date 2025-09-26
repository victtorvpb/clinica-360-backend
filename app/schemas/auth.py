from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.user import UserType


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    user: "UserResponse"


class TokenData(BaseModel):
    email: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    type_user: UserType
    is_active: bool
    is_superuser: bool
    created_at: str
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str
    type_user: UserType = UserType.SECRETARY


class UserUpdate(BaseModel):
    name: Optional[str] = None
    type_user: Optional[UserType] = None
    is_active: Optional[bool] = None


# Update forward references
TokenResponse.model_rebuild()
