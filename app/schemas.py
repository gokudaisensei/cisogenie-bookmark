from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl


# User schemas
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Bookmark schemas
class BookmarkBase(BaseModel):
    url: HttpUrl
    title: str
    description: Optional[str] = None
    category: Optional[str] = "General"


class BookmarkCreate(BookmarkBase):
    pass


class BookmarkUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None


class BookmarkResponse(BookmarkBase):
    id: int
    created_at: datetime
    updated_at: datetime
    owner_id: int

    class Config:
        from_attributes = True


# Authentication schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str
