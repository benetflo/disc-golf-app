from db_operations.db_manager import DBManager

class Layout:
    
    def __init__(self, course_name: str, name: str, description: str):
        self._course_name = course_name
        self._name = name
        self._description = description

    @property
    def course_name(self):
        return self._course_name

    @property
    def name(self):
        return self._name
                     
    @property
    def description(self):
        return self._description

    def insert_new_layout(self, db: DBManager):
        
        row = db.fetch_one(
            "SELECT id FROM courses WHERE name = %s;",
            (self._course_name,)
        )
        
        if row is not None:
            course_id = row[0]
            db.execute(
                "INSERT INTO layouts (course_id, name, description) VALUES (%s, %s, %s);",
                (course_id, self._name, self._description)
            )
            return 0
        
        return 1