from db_operations.db_manager import DBManager


class Course:
    
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location

    @property
    def name(self):
        return self._name
                     
    @property
    def location(self):
        return self._location

    def insert_new_course_to_db(self, db: DBManager) -> bool:
        
        # Check if course is already in DB
        row = db.fetch_one(
            "SELECT name FROM courses WHERE name = %s;",
            (self._name,)
        )

        # Insert into courses
        if row is None:
            db.execute(
                "INSERT INTO courses (name, location) VALUES (%s, %s);",
                (self._name, self._location)
            )
            return True
        
        return False
    
        # fill empty class object with excisting info from player in database
    @classmethod 
    def get_course_info_from_db(self, db: DBManager, name: str) -> dict:

        row = db.fetch_one(
            "SELECT * FROM courses WHERE name = %s;",
            (name,)
        )
        return row
        # add all info to class attributes not return row