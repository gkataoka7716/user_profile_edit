from pydantic import BaseModel, Field
from datetime import date

class UserinfoCreateRequest(BaseModel):
    birthday: date | None = None
    gender_id: int | None = None
    phone_number: str | None = Field(default=None, max_length=20)
    postal_code: str | None = Field(default=None, max_length=10)
    prefecture_id: int | None = None

class UserInfoUpdateRequest(BaseModel):
    birthday: date | None = None
    gender_id: int | None = None
    phone_number: str | None = Field(default=None, max_length=20)
    postal_code: str | None = Field(default=None, max_length=10)
    prefecture_id: int | None = None

class UserInfoResponse(BaseModel):
    id: int
    user_id: int
    birthday: date | None
    phone_number: str | None
    postal_code: str | None
    gender_id: int | None
    prefecture_id: int | None