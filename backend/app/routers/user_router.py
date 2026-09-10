from fastapi import APIRouter
from database import DbSession

from app.schemas.user_schema import UserRegisterRequest, UserLoginRequest, UserUpdateRequest

router = APIRouter()

# ユーザー登録
@router.post("/register")
async def create_user(user: UserRegisterRequest, db: DbSession):
    pass


# ログイン
@router.post("/login")
async def login_user(user: UserLoginRequest, db: DbSession):
    pass


# 全ユーザー取得
@router.get("/users")
async def get_users():
    pass


# ユーザー取得
@router.get("/users/{user_id}")
async def get_user(user_id: int):
    pass


# ユーザー情報更新
@router.patch("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdateRequest, db: DbSession):
    pass


# ユーザー削除
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    pass