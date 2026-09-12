from sqlalchemy import Column, Integer, String
from database.database import Base

class Prefectures(Base):
	__tablename__ = 'prefectures'

	id = Column(Integer, primary_key=True)
	name = Column(String(50), nullable=False, unique=True)