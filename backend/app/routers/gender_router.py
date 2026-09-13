from fastapi import APIRouter, HTTPException
from fastapi import Depends
from database.database import DbSession
from database.models.users import User
import logging

from app.schemas.gender_schema import (
    GenderCreateRequest,
    GenderUpdateRequest
)
from app.services import gender_service
from app.exception.database_exception import DatabaseError
from app.auth.dependencies import get_current_user


router = APIRouter()

logger = logging.getLogger(__name__)


# 性別登録
@router.post("/genders")
async def create_gender(
    gender: GenderCreateRequest,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    logger.info("[INFO] 性別登録を開始します。")

    try:
        request = gender_service.create_gender(gender, db)

        logger.info("[INFO] 性別登録が完了しました。")

        return request

    except DatabaseError as e:
        logger.error("[ERROR] 性別登録に失敗しました。")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# 登録した性別をすべて取得
@router.get("/genders")
async def get_genders(
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    logger.info("[INFO] 登録済み性別の取得を開始します。")

    try:
        request = gender_service.get_genders(db)

        logger.info("[INFO] 登録済み性別の取得が完了しました。")

        return request

    except DatabaseError as e:
        logger.error("[ERROR] 登録済み性別の取得に失敗しました。")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# 特定の性別取得
@router.get("/genders/{gender_id}")
async def get_gender(
    gender_id: int,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    logger.info(f"[INFO] 性別の取得を開始します。gender_id={gender_id}")

    try:
        request = gender_service.get_gender(gender_id, db)

        logger.info(f"[INFO] 性別の取得が完了しました。gender_id={gender_id}")

        return request

    except DatabaseError as e:
        logger.error(
            f"[ERROR] 性別の取得に失敗しました。gender_id={gender_id}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# 特定の性別名の変更
@router.put("/genders/{gender_id}")
async def update_gender(
    gender_id: int,
    gender: GenderUpdateRequest,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    logger.info(f"[INFO] 性別の更新を開始します。gender_id={gender_id}")

    try:
        request = gender_service.update_gender(
            gender_id,
            gender,
            db
        )

        logger.info(f"[INFO] 性別の更新が完了しました。gender_id={gender_id}")

        return request

    except DatabaseError as e:
        logger.error(
            f"[ERROR] 性別の更新に失敗しました。gender_id={gender_id}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# 特定の性別を削除
@router.delete("/genders/{gender_id}")
async def delete_gender(
    gender_id: int,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    logger.info(f"[INFO] 性別の削除を開始します。gender_id={gender_id}")

    try:
        request = gender_service.delete_gender(
            gender_id,
            db
        )

        logger.info(f"[INFO] 性別の削除が完了しました。gender_id={gender_id}")

        return request

    except DatabaseError as e:
        logger.error(
            f"[ERROR] 性別の削除に失敗しました。gender_id={gender_id}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )