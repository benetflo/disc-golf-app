# from routes.db_manager import DBManager as db

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
				name TEXT NOT NULL,
				username TEXT NOT NULL
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

	db.execute("""
		CREATE TABLE IF NOT EXISTS player_bags (
			id SERIAL PRIMARY KEY,
			player_id INT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
			disc_molds_id INT NOT NULL REFERENCES disc_molds(id) ON DELETE CASCADE
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