from pydantic import BaseModel, Field

class PrefecturesResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
