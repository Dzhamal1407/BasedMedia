from pydantic import BaseModel, EmailStr
from .models import UserModel
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    email_username: str | EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None




UserOut = pydantic_model_creator(
    UserModel,
    name='UserOut',
    exclude=('password',)
)
