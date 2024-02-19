from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class ContactModel(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    phone_no: str
    date_of_birth: date
    description: Optional[str] = ""


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=10)
    email: str
    password: str = Field(min_length=8, max_length=15)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr
