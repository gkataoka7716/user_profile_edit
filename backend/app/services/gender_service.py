from sqlalchemy.orm import Session
from database.models.genders import Gender

def create_gender(gender, db: Session):
	gender = Gender(name=gender)
	try:
		db.add(gender)
		db.commit()
		db.refresh()
	except:
		db.rollback()
		raise

	return 

