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

    def insert_new_course(self, db: DBManager):
        
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
            return 0
        
        return 1