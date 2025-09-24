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
	
	def fetch_one(self, query, params=None):
		"""
			Method to fetch one entry from a table
		"""
		conn = self.get_conn()

		try:
			with conn.cursor() as cur:
				cur.execute(query, params or ())
				return cur.fetchone()
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
