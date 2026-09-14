from fastapi import FastAPI
from contextlib import asynccontextmanager

from database.database import engine, Base, SessionLocal

from app.routers import userinfo_router, gender_router, prefectures_router, user_router
from app.services.gender_service import initialize_genders
from app.services.prefectures_service import create_prefectures

# 起動時に１回動作する
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("アプリを起動します")

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        initialize_genders(db)
        create_prefectures(db)
        yield
    finally:
        db.close()
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