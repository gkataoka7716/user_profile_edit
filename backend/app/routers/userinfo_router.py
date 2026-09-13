from fastapi import APIRouter, Depends

from database.database import DbSession
from database.models.users import User

from app.auth.dependencies import get_current_user

from app.schemas.userinfo_schema import (
    UserinfoCreateRequest,
    UserInfoUpdateRequest,
)

from app.services import userinfo_service


router = APIRouter()


# あるユーザーの情報を取得
@router.get("/user_info/{user_id}")
async def get_user_info(
    user_id: int,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    return userinfo_service.get_user_info(
        user_id,
        db,
    )


# あるユーザーの情報を登録
@router.post("/user_info/{user_id}")
async def create_user_info(
    user_id: int,
    userinfo: UserinfoCreateRequest,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    return userinfo_service.create_user_info(
        user_id,
        userinfo,
        db,
    )


# あるユーザーの情報を更新
@router.patch("/user_info/{user_id}")
async def update_user_info(
    user_id: int,
    userinfo: UserInfoUpdateRequest,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    return userinfo_service.update_user_info(
        user_id,
        userinfo,
        db,
    )