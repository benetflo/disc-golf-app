from psycopg2 import pool

class DBManager:

	def __init__(self):
		self.db_pool = pool.ThreadedConnectionPool(
	minconn=1,
	maxconn=10,
	dbname="discgolf_db",
	user="admin",
	password="kuk",
	host="0.0.0.0"
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
                name TEXT NOT NULL,
                location TEXT NOT NULL
        );
        """)
	
	db.execute("""
		CREATE TABLE IF NOT EXISTS players (
				id SERIAL PRIMARY KEY,
				name TEXT NOT NULL 
		);	  
		""")

if __name__ == "__main__":
	db = DBManager()
	init_tables(db)

	from players import register_new_player
	register_new_player(db, "Simon")
	register_new_player(db, "Benjamin")

	from courses import register_new_course
	register_new_course(db, "Rudan", "Haninge")
