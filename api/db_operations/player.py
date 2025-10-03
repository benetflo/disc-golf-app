from db_operations.db_manager import DBManager


class Player:

    def __init__(self, name=None, username=None, id=None):
        self._name = name
        self._username = username
        self._id = id

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
        
        if row is None: # checka så att klassens attribut inte är None så att man inte kan sätta in en tom Player klass

            db.execute(
                "INSERT INTO players (name, username) VALUES (%s, %s);",
                (self.name, self._username)
            )
            return True
        
        return False
    
    # fill empty class object with excisting info from player in database
    @classmethod 
    def get_player_info(self, db: DBManager, username):

        row = db.fetch_one(
            "SELECT * FROM players WHERE username = %s;",
            (username,)
        )
        return row
        # add all info to class attributes not return row
