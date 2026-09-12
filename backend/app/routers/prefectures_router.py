from fastapi import APIRouter, HTTPException

import logging

from database.database import DbSession
from app.services import prefectures_service
from app.exception.database_exception import DatabaseError

router = APIRouter()
logger = logging.getLogger()

# 47都道府県取得
@router.get("/prefectures")
def get_prefectures(db: DbSession):
    try:
        logger.info("[info] 47都道府県取得を開始します。")
        response = prefectures_service.get_prefectures(db)
        logger.info("[info] 47都道府県取得が完了しました。")
    except DatabaseError as e:
        raise HTTPException(staus_code=500, detail=str(e))

    return response