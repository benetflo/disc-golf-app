from db_manager import DBManager as db


# COURSE, LAYOUT, HOLE FUNCTIONS

def register_new_course(db, name, location):
	db.execute(
		"INSERT INTO courses (name, location) VALUES (%s, %s);",
		(name, location)
	)

def register_new_layout(db, course_id, name, holes_amount, description):
	db.execute(
		"INSERT INTO layouts (course_id, name, holes_amount, description) VALUES (%s, %s, %s, %s);",
		(course_id, name, holes_amount, description)
	)

def register_new_hole(db, layout_id, hole_num, par, distance, description):
	db.execute(
		"INSERT INTO holes (layout_id, hole_num, par, distance, description) VALUES (%s, %s, %s, %s, %s);",
		(layout_id, hole_num, par, distance, description)
	)
