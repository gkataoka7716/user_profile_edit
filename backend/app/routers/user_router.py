from fastapi import APIRouter, Depends, HTTPException
from database.database import DbSession
from database.models.users import User
import logging

from app.auth.dependencies import get_current_user

from app.schemas.user_schema import (
    UserRegisterRequest,
    UserLoginRequest,
    UserUpdateRequest,
)
from app.services import user_service
from app.exception.database_exception import (
    DatabaseError,
    UserAlreadyExistsError,
    UserNotFoundError,
)

router = APIRouter()
logger = logging.getLogger()


# ユーザー登録
@router.post("/register")
async def create_user(
    user: UserRegisterRequest,
    db: DbSession,
):
    logger.info("[INFO] ユーザー登録処理を開始します。")

    try:
        result = user_service.create_user(user, db)

        return result

    except UserAlreadyExistsError as e:
        logger.warning(
            "[WARNING] ユーザーはすでに登録されています。"
        )
        raise HTTPException(
            status_code=409,
            detail=str(e),
        )

    except DatabaseError:
        logger.error(
            "[ERROR] ユーザー登録処理に失敗しました。"
        )
        raise HTTPException(
            status_code=500,
            detail="ユーザー登録に失敗しました。",
        )


# ログイン
@router.post("/login")
async def login_user(
    user: UserLoginRequest,
    db: DbSession,
):
    logger.info("[INFO] ログイン処理を開始します。")

    try:
        result = user_service.login_user(user, db)

        return result

    except UserNotFoundError as e:
        logger.warning(
            "[WARNING] ログインに失敗しました。"
        )
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )

    except DatabaseError:
        logger.error(
            "[ERROR] ログイン処理に失敗しました。"
        )
        raise HTTPException(
            status_code=500,
            detail="ログイン処理に失敗しました。",
        )


# 全ユーザー取得
@router.get("/users")
async def get_users(
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    logger.info("[INFO] 全ユーザー取得処理を開始します。")

    try:
        result = user_service.get_users(db)

        return result

    except DatabaseError:
        logger.error(
            "[ERROR] 全ユーザーの取得に失敗しました。"
        )
        raise HTTPException(
            status_code=500,
            detail="ユーザーの取得に失敗しました。",
        )


# ユーザー取得
@router.get("/users/{user_id}")
async def get_user(
    user_id: int,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    logger.info(
        f"[INFO] ユーザー取得処理を開始します。id={user_id}"
    )

    try:
        result = user_service.get_user(user_id, db)

        return result

    except UserNotFoundError as e:
        logger.warning(
            f"[WARNING] ユーザーが存在しません。id={user_id}"
        )
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    except DatabaseError:
        logger.error(
            "[ERROR] ユーザーの取得に失敗しました。"
        )
        raise HTTPException(
            status_code=500,
            detail="ユーザーの取得に失敗しました。",
        )


# ユーザー情報更新
@router.patch("/users/{user_id}")
async def update_user(
    user_id: int,
    user: UserUpdateRequest,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    logger.info(
        f"[INFO] ユーザー更新処理を開始します。id={user_id}"
    )

    try:
        result = user_service.update_user(
            user_id,
            user,
            db,
        )

        return result

    except UserNotFoundError as e:
        logger.warning(
            f"[WARNING] ユーザーが存在しません。id={user_id}"
        )
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    except UserAlreadyExistsError as e:
        logger.warning(
            "[WARNING] 変更後のユーザー名はすでに使用されています。"
        )
        raise HTTPException(
            status_code=409,
            detail=str(e),
        )

    except DatabaseError:
        logger.error(
            "[ERROR] ユーザー更新処理に失敗しました。"
        )
        raise HTTPException(
            status_code=500,
            detail="ユーザー情報の更新に失敗しました。",
        )


# ユーザー削除
@router.delete("/users/{user_id}")
async def delete_user(
    user_id: int,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    logger.info(
        f"[INFO] ユーザー削除処理を開始します。id={user_id}"
    )

    try:
        result = user_service.delete_user(
            user_id,
            db,
        )

        return result

    except UserNotFoundError as e:
        logger.warning(
            f"[WARNING] ユーザーが存在しません。id={user_id}"
        )
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    except DatabaseError:
        logger.error(
            "[ERROR] ユーザー削除処理に失敗しました。"
        )
        raise HTTPException(
            status_code=500,
            detail="ユーザーの削除に失敗しました。",
        )
