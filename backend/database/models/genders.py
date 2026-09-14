from sqlalchemy import Column, Integer, String
from database.database import Base

class Genders(Base):
	__tablename__ = 'genders'

	id = Column(Integer, primary_key=True)
	name = Column(String(50), unique=True, nullable=False)