from fastapi import FastAPI
from contextlib import asynccontextmanager

from database.database import engine, Base

from app.routers import userinfo_router, gender_router, prefectures_router, user_router

# 起動時に１回動作する
@asynccontextmanager
async def lifespan(app: FastAPI):
    # アプリ起動時
    print("アプリを起動します")

    # テーブル作成
    Base.metadata.create_all(bind=engine)

    yield

    # アプリ終了時
    print("アプリを終了します")


app = FastAPI(lifespan=lifespan)

app.include_router(user_router.router, prefix="/v1")
app.include_router(gender_router.router, prefix="/v1")
app.include_router(prefectures_router.router, prefix="/v1")
app.include_router(userinfo_router.router, prefix="/v1")

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)