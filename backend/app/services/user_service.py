from database.database import DbSession
from app.schemas.user_schema import (
    UserRegisterRequest,
    UserLoginRequest,
    UserUpdateRequest,
)
from database.models.users import User
import logging

from app.auth.security import create_access_token
from app.exception.database_exception import (
    DatabaseError,
    UserAlreadyExistsError,
    UserNotFoundError,
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)

logger = logging.getLogger()


# ユーザー登録
def create_user(user: UserRegisterRequest, db: DbSession):
    try:
        if _user_exists(user.username, db):
            raise UserAlreadyExistsError(
                "ユーザーはすでに登録されています。"
            )

        hashed_password = _password_hash(user.password)

        new_user = User(
            username=user.username,
            password=hashed_password,
            role=user.role
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        logger.info("[INFO] ユーザーを登録しました。")

        return new_user

    except UserAlreadyExistsError:
        raise

    except Exception as e:
        db.rollback()
        logger.error(
            f"[ERROR] ユーザー登録に失敗しました: {e}"
        )
        raise DatabaseError()


# ログイン
def login_user(user: UserLoginRequest, db: DbSession):
    try:
        db_user = _get_user_by_name(user.username, db)

        if db_user is None:
            raise UserNotFoundError(
                "ユーザーが存在しません。"
            )

        if not check_password_hash(
            db_user.password,
            user.password,
        ):
            raise UserNotFoundError(
                "ユーザー名またはパスワードが正しくありません。"
            )

        access_token = create_access_token(db_user.id)

        logger.info("[INFO] ログインに成功しました。")

        return {
            "message": "ログインに成功しました。",
            "access_token": access_token,
            "user_id": db_user.id,
            "username": db_user.username,
        }

    except UserNotFoundError:
        raise

    except Exception as e:
        logger.error(
            f"[ERROR] ログイン処理に失敗しました: {e}"
        )
        raise DatabaseError()


# 全ユーザー取得
def get_users(db: DbSession):
    try:
        users = db.query(User.username).order_by(User.id).scalars().all()

        logger.info("[INFO] 全ユーザーを取得しました。")

        return users

    except Exception as e:
        logger.error(
            f"[ERROR] 全ユーザー取得に失敗しました: {e}"
        )
        raise DatabaseError()


# ユーザー取得
def get_user(user_id: int, db: DbSession):
    try:
        user = get_user_by_id(user_id, db)

        if user is None:
            raise UserNotFoundError(
                "指定されたユーザーは存在しません。"
            )

        return user

    except UserNotFoundError:
        raise

    except Exception as e:
        logger.error(
            f"[ERROR] ユーザー取得に失敗しました: {e}"
        )
        raise DatabaseError()


# ユーザー情報更新
def update_user(
    user_id: int,
    request: UserUpdateRequest,
    db: DbSession,
):
    try:
        user = get_user_by_id(user_id, db)

        if user is None:
            raise UserNotFoundError(
                "指定されたユーザーは存在しません。"
            )

        # usernameが変更される場合
        if request.username is not None:

            # 自分以外のユーザーが同じ名前を使用していないか確認
            existing_user = _get_user_by_name(
                request.username,
                db,
            )

            if (
                existing_user is not None
                and existing_user.id != user_id
            ):
                raise UserAlreadyExistsError(
                    "そのユーザー名はすでに使用されています。"
                )

            user.username = request.username

        # passwordが変更される場合
        if request.password is not None:
            user.password = _password_hash(
                request.password
            )

        # roleが変更される場合
        if request.role is not None:
            user.role = request.role.value

        db.commit()
        db.refresh(user)

        logger.info(
            f"[INFO] ユーザー情報を更新しました。id={user_id}"
        )

        return user

    except (
        UserNotFoundError,
        UserAlreadyExistsError,
    ):
        raise

    except Exception as e:
        db.rollback()
        logger.error(
            f"[ERROR] ユーザー更新に失敗しました: {e}"
        )
        raise DatabaseError()


# ユーザー削除
def delete_user(user_id: int, db: DbSession):
    try:
        user = get_user_by_id(user_id, db)

        if user is None:
            raise UserNotFoundError(
                "指定されたユーザーは存在しません。"
            )

        db.delete(user)
        db.commit()

        logger.info(
            f"[INFO] ユーザーを削除しました。id={user_id}"
        )

        return {
            "message": "ユーザーを削除しました。"
        }

    except UserNotFoundError:
        raise

    except Exception as e:
        db.rollback()
        logger.error(
            f"[ERROR] ユーザー削除に失敗しました: {e}"
        )
        raise DatabaseError()


# ユーザー名から取得
def _get_user_by_name(
    username: str,
    db: DbSession,
):
    try:
        return (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

    except Exception as e:
        logger.error(
            f"[ERROR] ユーザー検索に失敗しました: {e}"
        )
        raise DatabaseError()


# IDから取得
def get_user_by_id(
    user_id: int,
    db: DbSession,
):
    try:
        return (
            db.query(User.username)
            .filter(User.id == user_id)
            .first()
        )

    except Exception as e:
        logger.error(
            f"[ERROR] ユーザー検索に失敗しました: {e}"
        )
        raise DatabaseError()


# ユーザーが存在するか確認
def _user_exists(
    username: str,
    db: DbSession,
) -> bool:
    return _get_user_by_name(username, db) is not None


# パスワードハッシュ化
def _password_hash(password: str) -> str:
    hashed_password = generate_password_hash(password)

    logger.info("[INFO] パスワードをハッシュ化しました。")

    return hashed_password