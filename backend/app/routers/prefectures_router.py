from fastapi import APIRouter

from database.database import DbSession
from app.services import prefectures_service

router = APIRouter()

# 47都道府県取得
@router.get("/prefectures")
def get_prefectures(db: DbSession):
    response = prefectures_service.get_prefectures(db)
    return response