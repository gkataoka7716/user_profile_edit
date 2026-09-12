from fastapi import APIRouter
from database.database import DbSession

from app.schemas.userinfo_schema import UserinfoCreateRequest, UserInfoUpdateRequest

router = APIRouter()

# あるユーザーの情報を取得
@router.get("/user_info/{user_id}")
async def get_user_info(user_id: int, db:DbSession):
	pass

# あるユーザーの情報を登録
@router.post("/user_info/{user_id}")
async def creat_user_info(user_id: int, userinfo: UserinfoCreateRequest, db:DbSession):
	pass

# あるユーザーの情報を更新
@router.patch("/user_info/{user_id}")
async def update_user_info(user_id: int, userinfo: UserInfoUpdateRequest, db:DbSession):
	pass


