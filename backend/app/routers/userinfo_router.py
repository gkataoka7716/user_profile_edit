from fastapi import APIRouter, Depends, HTTPException

from database.database import DbSession
from database.models.users import User

from app.auth.dependencies import get_current_user

from app.schemas.userinfo_schema import (
    UserinfoCreateRequest,
    UserInfoUpdateRequest,
    UserInfoResponse,
)

from app.services import userinfo_service
from app.exception.database_exception import (
    DatabaseError,
    UserAlreadyExistsError,
    UserNotFoundError,
)


router = APIRouter()


# あるユーザーの情報を取得
@router.get("/user_info/{user_id}", respomse_model=UserInfoResponse)
async def get_user_info(
    user_id: int,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    try:
        return userinfo_service.get_user_info(user_id, db)
    except UserNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except DatabaseError:
        raise HTTPException(status_code=500, detail="ユーザー情報の取得に失敗しました。")


# あるユーザーの情報を登録
@router.post("/user_info/{user_id}")
async def create_user_info(
    user_id: int,
    userinfo: UserinfoCreateRequest,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    try:
        return userinfo_service.create_user_info(user_id, userinfo, db)
    except UserNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except UserAlreadyExistsError as error:
        raise HTTPException(status_code=409, detail=str(error))
    except DatabaseError:
        raise HTTPException(status_code=500, detail="ユーザー情報の登録に失敗しました。")


# あるユーザーの情報を更新
@router.patch("/user_info/{user_id}")
async def update_user_info(
    user_id: int,
    userinfo: UserInfoUpdateRequest,
    db: DbSession,
    current_user: User = Depends(get_current_user),
):
    try:
        return userinfo_service.update_user_info(user_id, userinfo, db)
    except UserNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except DatabaseError:
        raise HTTPException(status_code=500, detail="ユーザー情報の更新に失敗しました。")