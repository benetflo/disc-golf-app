from routes.db_manager import DBManager as db

def insert_new_player(db, name, username):
    
    row = db.fetch_one(
        "SELECT username FROM players WHERE username = %s;",
        (username,)
    )
    
    if row is None:

        db.execute(
            "INSERT INTO players (name, username) VALUES (%s, %s);",
            (name, username)
        )
        return 0
    
    return 1