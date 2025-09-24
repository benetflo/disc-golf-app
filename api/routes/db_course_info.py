from routes.db_manager import DBManager as db


# COURSE, LAYOUT, HOLE FUNCTIONS

def insert_new_course(db, name, location):
	
	# Check if course is already in DB
	row = db.fetch_one(
		"SELECT name FROM courses WHERE name = %s;",
		(name,)
	)

	# Insert into courses
	if row is None:
		db.execute(
			"INSERT INTO courses (name, location) VALUES (%s, %s);",
			(name, location)
		)
		return 0
	
	return 1

def insert_new_layout(db, course_name, name, description):
	
	row = db.fetch_one(
		"SELECT id FROM courses WHERE name = %s;",
		(course_name,)
	)
	
	if row is not None:
		course_id = row[0]
		db.execute(
			"INSERT INTO layouts (course_id, name, description) VALUES (%s, %s, %s);",
			(course_id, name, description)
		)
		return 0
	
	return 1

def insert_new_hole(db, layout_id, hole_num, par, distance, description):
	db.execute(
		"INSERT INTO holes (layout_id, hole_num, par, distance, description) VALUES (%s, %s, %s, %s, %s);",
		(layout_id, hole_num, par, distance, description)
	)
