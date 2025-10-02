from db_operations.db_manager import DBManager as db


class Player:

    def __init__(self, name: str, username: str):
        self._name = name
        self._username = username

    @property
    def username(self):
        return self._username
                     
    @property
    def name(self):
        return self._name

    def insert_player_to_db(self, db: DBManager):
        
        row = db.fetch_one(
            "SELECT username FROM players WHERE username = %s;",
            (self._username,)
        )
        
        if row is None:

            db.execute(
                "INSERT INTO players (name, username) VALUES (%s, %s);",
                (self.name, self._username)
            )
            return True
        
        return False