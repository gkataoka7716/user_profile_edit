from fastapi import APIRouter

from app.schemas.gender_schema import GenderCreateRequest, GenderUpdateRequest

router = APIRouter()

# 性別登録
@router.post("/genders")
async def create_gender():
    pass

# 登録した性別をすべて取得
@router.get("/genders")
async def get_genders():
    pass

# 特定の性別取得
@router.get("/genders/{gender_id}")
async def get_gender(gender_id: int, gender: GenderCreateRequest):
    pass

# 特定の性別名の変更
@router.put("/genders/{gender_id}")
async def update_gender(gender_id: int, gender: GenderUpdateRequest):
    pass

# 特定の性別を削除
@router.delete("/genders/{gender_id}")
async def delete_gender(gender_id: int):
    pass