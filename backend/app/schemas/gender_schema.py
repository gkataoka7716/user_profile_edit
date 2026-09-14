from pydantic import BaseModel, Field

class GenderCreateRequest(BaseModel):
	name: str = Field(...)

class GenderUpdateRequest(BaseModel):
	name: str = Field(...)