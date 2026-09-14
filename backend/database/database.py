import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base


load_dotenv()


# DB接続
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


# モデルの基底クラス
Base = declarative_base()


# セッションの作成
SessionLocal = sessionmaker(bind=engine)


# セッションを取得するための関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# DBセッション用の型
DbSession = Annotated[Session, Depends(get_db)]