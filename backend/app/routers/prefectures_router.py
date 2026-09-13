from fastapi import APIRouter, Depends, HTTPException

import logging

from database.database import DbSession
from database.models.users import User
from app.auth.dependencies import get_current_user
from app.services import prefectures_service
from app.exception.database_exception import DatabaseError

router = APIRouter()
logger = logging.getLogger()

# 47都道府県取得
@router.get("/prefectures")
def get_prefectures(
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    try:
        logger.info("[info] 47都道府県取得を開始します。")
        response = prefectures_service.get_prefectures(db)
        logger.info("[info] 47都道府県取得が完了しました。")
    except DatabaseError as e:
        raise HTTPException(staus_code=500, detail=str(e))

    return response
