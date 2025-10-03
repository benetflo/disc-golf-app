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

    def insert_hole_to_db(self, db: DBManager, course_name: str, layout_name: str, hole_order: int) -> bool:
        
        row = db.fetch_one(
            "SELECT id FROM courses WHERE name = %s;",
            (course_name,)
        )

        if row is not None:
            course_id = row[0]

            hole_id = db.execute_returning_id(
                "INSERT INTO holes (course_id, distance, par, description) VALUES (%s, %s, %s, %s) RETURNING id;",
                (course_id, self._distance, self._par, self._description)
            )

            # get the layout id
            row = db.fetch_one(
                "SELECT id FROM layouts WHERE name = %s;",
                (layout_name,)
            )
            layout_id = row[0]

            db.execute(
                "INSERT INTO holes_in_layouts (layout_id, hole_id, hole_order) VALUES (%s, %s, %s);",
                (layout_id, hole_id, hole_order)
            )

            return True
        
        return False
 
    def get_holes_in_course_info_from_db(db: DBManager, course_name: str) -> tuple:
            
            row = db.fetch_one(
                "SELECT id FROM courses WHERE name = %s;",
            (course_name,)
            )
            
            # if course exists
            if row is not None:
                course_id = row[0]
                holes = db.fetch_all(
                    "SELECT * FROM holes WHERE course_id = %s;",
                    (course_id,)
                )
                return holes
            
            return (None,)
            


                 