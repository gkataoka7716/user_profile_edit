from sqlalchemy import Session, SQLAlchemyError

from database.models.prefectures import Prefectures
from app.exception.database_exception import DatabaseError


import logging


PREFECTURES = [
    "北海道",
    "青森県",
    "岩手県",
    "宮城県",
    "秋田県",
    "山形県",
    "福島県",
    "茨城県",
    "栃木県",
    "群馬県",
    "埼玉県",
    "千葉県",
    "東京都",
    "神奈川県",
    "新潟県",
    "富山県",
    "石川県",
    "福井県",
    "山梨県",
    "長野県",
    "岐阜県",
    "静岡県",
    "愛知県",
    "三重県",
    "滋賀県",
    "京都府",
    "大阪府",
    "兵庫県",
    "奈良県",
    "和歌山県",
    "鳥取県",
    "島根県",
    "岡山県",
    "広島県",
    "山口県",
    "徳島県",
    "香川県",
    "愛媛県",
    "高知県",
    "福岡県",
    "佐賀県",
    "長崎県",
    "熊本県",
    "大分県",
    "宮崎県",
    "鹿児島県",
    "沖縄県",
]

logger = logging.getLogger()


def create_prefectures(db: Session):

	# すでに登録されていれば何もしない
    if db.query(Prefectures).first() is not None:
        logger.info("[info] 47都道府県は登録済みです。")
        return
    
    try:
        for name in PREFECTURES:
            db.add(Prefectures(name=name))

        db.commit()
        logger.info("[info] 47都道府県を登録しました。")
    except Exception:
        db.rollback()
        logger.error("[エラー] 47都道府県の登録に失敗しました。")
        raise DatabaseError("47都道府県の登録に失敗しました。")


def get_prefectures(db: Session) -> list[Prefectures]:

    try:
        prefectures = db.query(Prefectures).order_by(Prefectures.id).all()

        if len(prefectures) != 47:
            logger.warning("[警告] 47都道府県が47個ありません。")

    except SQLAlchemyError:
        logger.error("[エラー] 47都道府県の取得に失敗しました")
        raise DatabaseError("47都道府県の取得に失敗しました")

    return prefectures