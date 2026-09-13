from enum import Enum

from pydantic import BaseModel, Field


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class UserRegisterRequest(BaseModel):
    username: str = Field(min_length=4, max_length=64)
    password: str
    role: UserRole

class UserLoginRequest(BaseModel):
    username: str = Field(min_length=4, max_length=64)
    password: str

class UserUpdateRequest(BaseModel):
    username: str | None = Field(default=None, min_length=4, max_length=64)
    password: str | None = None
    role: UserRole | None = None

class UserUpdateResponse(BaseModel):
    id: int
    username: str = Field(min_length=4, max_length=64)
    role: UserRole

class UserRegisterResponse(BaseModel):
    id: int
    username: str = Field(min_length=4, max_length=64)
    role: UserRole

class UserLoginResponse(BaseModel):
    id: int
    username: str = Field(min_length=4, max_length=64)
    role: UserRole