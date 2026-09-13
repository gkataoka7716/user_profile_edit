import logging

from database.database import DbSession
from database.models.userinfo import UserInfo

from app.schemas.userinfo_schema import (
    UserinfoCreateRequest,
    UserInfoUpdateRequest,
)

from app.exception.database_exception import (
    DatabaseError,
    UserAlreadyExistsError,
    UserNotFoundError,
)


logger = logging.getLogger(__name__)


# ユーザー情報取得
def get_user_info(
    user_id: int,
    db: DbSession,
):
    try:
        user = (
            db.query(UserInfo)
            .filter(UserInfo.id == user_id)
            .first()
        )

        if user is None:
            raise UserNotFoundError(
                "指定されたユーザーは存在しません。"
            )

        user_info = (
            db.query(UserInfo)
            .filter(UserInfo.user_id == user_id)
            .first()
        )

        if user_info is None:
            raise UserNotFoundError(
                "ユーザー情報が登録されていません。"
            )

        return user_info

    except UserNotFoundError:
        raise

    except Exception as e:
        logger.error(
            f"[ERROR] ユーザー情報取得に失敗しました: {e}"
        )
        raise DatabaseError()


# ユーザー情報登録
def create_user_info(
    user_id: int,
    UserInfo: UserinfoCreateRequest,
    db: DbSession,
):
    try:
        user = (
            db.query(UserInfo)
            .filter(UserInfo.id == user_id)
            .first()
        )

        if user is None:
            raise UserNotFoundError(
                "指定されたユーザーは存在しません。"
            )

        existing_user_info = (
            db.query(UserInfo)
            .filter(UserInfo.user_id == user_id)
            .first()
        )

        if existing_user_info is not None:
            raise UserAlreadyExistsError(
                "ユーザー情報はすでに登録されています。"
            )

        new_user_info = UserInfo(
            user_id=user_id,
            birthday=UserInfo.birthday,
            gender_id=UserInfo.gender_id,
            phone_number=UserInfo.phone_number,
            postal_code=UserInfo.postal_code,
            prefecture_id=UserInfo.prefecture_id,
        )

        db.add(new_user_info)
        db.commit()
        db.refresh(new_user_info)

        logger.info(
            f"[INFO] ユーザー情報を登録しました。user_id={user_id}"
        )

        return new_user_info

    except (
        UserNotFoundError,
        UserAlreadyExistsError,
    ):
        raise

    except Exception as e:
        db.rollback()

        logger.error(
            f"[ERROR] ユーザー情報登録に失敗しました: {e}"
        )

        raise DatabaseError()


# ユーザー情報更新
def update_user_info(
    user_id: int,
    UserInfo: UserInfoUpdateRequest,
    db: DbSession,
):
    try:
        user_info = (
            db.query(UserInfo)
            .filter(UserInfo.user_id == user_id)
            .first()
        )

        if user_info is None:
            raise UserNotFoundError(
                "ユーザー情報が登録されていません。"
            )

        if UserInfo.birthday is not None:
            user_info.birthday = UserInfo.birthday

        if UserInfo.gender_id is not None:
            user_info.gender_id = UserInfo.gender_id

        if UserInfo.phone_number is not None:
            user_info.phone_number = UserInfo.phone_number

        if UserInfo.postal_code is not None:
            user_info.postal_code = UserInfo.postal_code

        if UserInfo.prefecture_id is not None:
            user_info.prefecture_id = UserInfo.prefecture_id

        db.commit()
        db.refresh(user_info)

        logger.info(
            f"[INFO] ユーザー情報を更新しました。user_id={user_id}"
        )

        return user_info

    except UserNotFoundError:
        raise

    except Exception as e:
        db.rollback()

        logger.error(
            f"[ERROR] ユーザー情報更新に失敗しました: {e}"
        )

        raise DatabaseError()