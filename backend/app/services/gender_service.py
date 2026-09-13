from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
import logging

from database.models.genders import Genders
from app.exception.database_exception import DatabaseError


logger = logging.getLogger()

# 性別マスタ初期登録
def initialize_genders(db: Session):
    gender_list = ["男性", "女性", "その他"]

    try:
        for name in gender_list:
            exists = (
                db.query(Genders)
                .filter(Genders.name == name)
                .first()
            )

            if exists is None:
                db.add(Genders(name=name))

        db.commit()

        logger.info("[INFO] 性別マスタの初期登録が完了しました。")

    except SQLAlchemyError:
        db.rollback()

        logger.exception(
            "[ERROR] 性別マスタの初期登録に失敗しました。"
        )

        raise DatabaseError(
            "性別マスタの初期登録に失敗しました。"
        )


# 性別登録
def create_gender(gender: str, db: Session):
    new_gender = Genders(name=gender)

    try:
        db.add(new_gender)
        db.commit()
        db.refresh(new_gender)

        logger.info("[INFO] 新しい性別の登録が完了しました。")

        return new_gender

    except SQLAlchemyError:
        db.rollback()

        logger.exception("[ERROR] 新しい性別の登録に失敗しました。")

        raise DatabaseError(
            "新しい性別の登録に失敗しました。"
        )


# 登録済み性別をすべて取得
def get_genders(db: Session):
    try:
        genders = (
            db.query(Genders)
            .order_by(Genders.id)
            .all()
        )

        logger.info("[INFO] 登録済み性別の取得が完了しました。")

        return genders

    except SQLAlchemyError:
        logger.exception("[ERROR] 登録済み性別の取得に失敗しました。")

        raise DatabaseError(
            "登録済み性別の取得に失敗しました。"
        )


# 特定の性別を取得
def get_gender(gender_id: int, db: Session):
    try:
        gender = (
            db.query(Genders)
            .filter(Genders.id == gender_id)
            .first()
        )

        if gender is None:
            raise ValueError("指定された性別が存在しません。")

        logger.info(
            f"[INFO] 性別の取得が完了しました。gender_id={gender_id}"
        )

        return gender

    except ValueError:
        raise

    except SQLAlchemyError:
        logger.exception(
            f"[ERROR] 性別の取得に失敗しました。gender_id={gender_id}"
        )

        raise DatabaseError(
            "性別の取得に失敗しました。"
        )


# 特定の性別名を変更
def update_gender(
    gender_id: int,
    gender_name: str,
    db: Session
):
    try:
        gender = (
            db.query(Genders)
            .filter(Genders.id == gender_id)
            .first()
        )

        if gender is None:
            raise ValueError("指定された性別が存在しません。")

        gender.name = gender_name

        db.commit()
        db.refresh(gender)

        logger.info(
            f"[INFO] 性別の更新が完了しました。gender_id={gender_id}"
        )

        return gender

    except ValueError:
        raise

    except SQLAlchemyError:
        db.rollback()

        logger.exception(
            f"[ERROR] 性別の更新に失敗しました。gender_id={gender_id}"
        )

        raise DatabaseError(
            "性別の更新に失敗しました。"
        )


# 特定の性別を削除
def delete_gender(gender_id: int, db: Session):
    try:
        gender = (
            db.query(Genders)
            .filter(Genders.id == gender_id)
            .first()
        )

        if gender is None:
            raise ValueError("指定された性別が存在しません。")

        db.delete(gender)
        db.commit()

        logger.info(
            f"[INFO] 性別の削除が完了しました。gender_id={gender_id}"
        )

        return gender

    except ValueError:
        raise

    except SQLAlchemyError:
        db.rollback()

        logger.exception(
            f"[ERROR] 性別の削除に失敗しました。gender_id={gender_id}"
        )

        raise DatabaseError(
            "性別の削除に失敗しました。"
        )