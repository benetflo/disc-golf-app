# from routes.db_manager import DBManager as db


# COURSE, LAYOUT, HOLE FUNCTIONS


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
	
