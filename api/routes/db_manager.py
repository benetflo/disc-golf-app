from psycopg2 import pool

class DBManager:

	def __init__(self):
		self.db_pool = pool.ThreadedConnectionPool(
	minconn=1,
	maxconn=10,
	dbname="discgolf_db",
	user="admin",
	password="kuk",
	host="db"
	)

	def get_conn(self):
		"""
			Helper method to get new connection from connection pool
		"""
		return self.db_pool.getconn()

	def put_conn(self, conn):
		"""
			Helper method to add connection back to connection pool
		"""
		self.db_pool.putconn(conn)

	def fetch_all(self, query, params=None):
		"""
			Method to fetch all entries from a table
		"""
		conn = self.get_conn()
		try:
			with conn.cursor as cur:
				cur.execute(query, params or ())
				return cur.fetchall()
		finally:
			self.put_conn(conn)

	def execute(self, query, params="None"):
		"""
			Method to execute a command/query in database
		"""
		conn = self.get_conn()
		try:
			with conn.cursor() as cur:
				cur.execute(query, params or ())
				conn.commit()
		finally:
			self.put_conn(conn)

def init_tables(db: DBManager):
	"""
	initialises all tables for the database
	"""

	db.execute("""
		CREATE TABLE IF NOT EXISTS courses (
			id SERIAL PRIMARY KEY,
			name TEXT NOT NULL,
			location TEXT NOT NULL
		);
		""")

	db.execute("""
        CREATE TABLE IF NOT EXISTS holes (
                id SERIAL PRIMARY KEY,
				course_id INT NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
                distance INT NOT NULL,
                par INT NOT NULL,
				description TEXT NOT NULL
        );
        """)

	db.execute("""
		CREATE TABLE IF NOT EXISTS layouts (
			id SERIAL PRIMARY KEY,
			course_id INT NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
			name TEXT NOT NULL,
			description TEXT NOT NULL
		);
		""")

	db.execute("""
        CREATE TABLE IF NOT EXISTS holes_in_layout (
			id SERIAL PRIMARY KEY,
			layout_id INT NOT NULL REFERENCES layouts(id) ON DELETE CASCADE,
			hole_id INT NOT NULL REFERENCES holes(id) ON DELETE CASCADE,
			hole_order INT NOT NULL
        );
        """)

#################################################################################################
	
	db.execute("""
		CREATE TABLE IF NOT EXISTS players (
				id SERIAL PRIMARY KEY,
				name TEXT NOT NULL
		);	  
		""")

	db.execute("""
		CREATE TABLE IF NOT EXISTS rounds (
				id SERIAL PRIMARY KEY,
				player_id INT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
				layout_id INT NOT NULL REFERENCES layouts(id) ON DELETE CASCADE,
				course_id INT NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
				date_played DATE NOT NULL
		);	  
		""")

	db.execute("""
		CREATE TABLE IF NOT EXISTS round_scores (
				id SERIAL PRIMARY KEY,
				round_id INT NOT NULL REFERENCES rounds(id) ON DELETE CASCADE,
				hole_id INT NOT NULL REFERENCES holes(id) ON DELETE CASCADE,
				throws INT NOT NULL
				
		);	  
		""")

	db.execute("""
		CREATE TABLE IF NOT EXISTS disc_molds (
				id SERIAL PRIMARY KEY,
				manifacturer TEXT NOT NULL, 
				name TEXT NOT NULL, 
				type TEXT NOT NULL, 
				speed TEXT NOT NULL,
				glide TEXT NOT NULL, 
				turn TEXT NOT NULL, 
				fade TEXT NOT NULL 
		);	  
		""")

	# "SELECT * FROM layout_with_total_par"          anywhere in code
	db.execute("""
		CREATE OR REPLACE VIEW layout_with_total_par AS
		SELECT
    		l.id AS layout_id,
    		l.name AS layout_name,
    		l.description,
    		l.course_id,
    		SUM(h.par) AS total_par
		FROM layouts l
		JOIN holes_in_layout hil ON hil.layout_id = l.id
		JOIN holes h ON h.id = hil.hole_id
		GROUP BY l.id, l.name, l.description, l.course_id
		ORDER BY l.id;
		""")

	# "SELECT * FROM round_scores_with_par WHERE round_id = 1;"			anywhere in code
	db.execute("""
		CREATE OR REPLACE VIEW round_scores_with_par AS
		SELECT
			rs.id AS round_score_id,
			rs.round_id,
			rs.hole_id,
			rs.throws,
			h.par AS hole_par,
			rs.throws - h.par AS score_vs_par
		FROM round_scores rs
		JOIN holes h ON h.id = rs.hole_id;
	""")

