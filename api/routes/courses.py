from db_manager import DBManager as db

def register_new_course(db, name, location):
	db.execute(
		"INSERT INTO courses (name, location) VALUES (%s, %s);",
		(name, location)
	)


