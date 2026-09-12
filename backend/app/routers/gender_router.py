from fastapi import APIRouter
from database.database import DbSession

from app.schemas.gender_schema import GenderCreateRequest, GenderUpdateRequest

router = APIRouter()

# 性別登録
@router.post("/genders")
async def create_gender(gender: GenderCreateRequest, db: DbSession):
    request = gender_service.create_gender(gender)
    return request

# 登録した性別をすべて取得
@router.get("/genders")
async def get_genders(db: DbSession):
    pass

# 特定の性別取得
@router.get("/genders/{gender_id}")
async def get_gender(gender_id: int, db: DbSession):
    pass

# 特定の性別名の変更
@router.put("/genders/{gender_id}")
async def update_gender(gender_id: int, gender: GenderUpdateRequest, db: DbSession):
    pass

# 特定の性別を削除
@router.delete("/genders/{gender_id}")
async def delete_gender(gender_id: int, db: DbSession):
    pass