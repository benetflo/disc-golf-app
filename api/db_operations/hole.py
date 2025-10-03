from db_operations.db_manager import DBManager

class Hole:

    def __init__(self, distance, par, description):
        self._distance = distance
        self._par = par
        self._description = description


    @property
    def distance(self):
        return self._distance

    @property
    def par(self):
        return self._par

    @property
    def description(self):
        return self._description

    def insert_new_hole(db: DBManager, course_name):
        
        row = db.fetch_one(
            "SELECT id FROM courses WHERE name = %s;",
            (course_name,)
        )

        if row is not None:
            course_id = row[0]
            db.execute(
                "INSERT INTO holes (course_id, distance, par, description) VALUES (%s, %s, %s, %s);",
                (course_id, self._distance, self._par, self._description)
            )
            return True
        
        return False