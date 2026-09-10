from pydantic import BaseModel, Field
from datetime import date

class UserinfoCreateRequest(BaseModel):
    birthday: date | None = None
    gender: str | None = None
    phone_number: str | None = Field(default=None, max_length=20)
    postal_code: str | None = Field(default=None, max_length=10)
    prefecture_id: str | None = None	

class UserInfoUpdateRequest(BaseModel):
    birthday: date | None = None
    gender: str | None = None
    phone_number: str | None = Field(default=None, max_length=20)
    postal_code: str | None = Field(default=None, max_length=10)
    prefecture_id: str | None = None