from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Date
from database.database import Base

class UserInfo(Base):
    __tablename__ = 'userinfo'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    birthday = Column(Date, nullable=True)
    gender_id = Column(Integer, ForeignKey('genders.id'), nullable=True)
    phone_number = Column(String(20), nullable=True)
    postal_code = Column(String(10), nullable=True)
    prefecture_id = Column(Integer, ForeignKey('prefectures.id'), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
