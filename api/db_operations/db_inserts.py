# from routes.db_manager import DBManager as db


# COURSE, LAYOUT, HOLE FUNCTIONS

def insert_new_hole(db, course_name, distance, par, description):
	
	row = db.fetch_one(
		"SELECT id FROM courses WHERE name = %s;",
		(course_name,)
	)

	if row is not None:
		course_id = row[0]
		db.execute(
			"INSERT INTO holes (course_id, distance, par, description) VALUES (%s, %s, %s, %s);",
			(course_id, distance, par, description)
		)
		return 0
	
	return 1

def insert_discs_from_csv(db: DBManager):
    csv_path = '/main/scripts/files/discs.csv'

    conn = db.get_conn()
    try:
        with conn.cursor() as cur, open(csv_path, 'r') as f:
            cur.copy_expert("""
                COPY disc_molds(manufacturer, name, type, speed, glide, turn, fade)
                FROM STDIN WITH CSV HEADER
            """, f)
        conn.commit()
        print("CSV file successfully imported to database")
    finally:
        db.put_conn(conn)
	
