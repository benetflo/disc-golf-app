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

    def insert_layout_to_db(self, db: DBManager) -> bool:
        
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
            return True
        
        return False
    
        # fill empty class object with excisting info from player in database
    @classmethod 
    def get_layout_info_from_db(cls, db: DBManager, course_name, layout_name) -> dict:

        row = db.fetch_one(
            "SELECT id FROM courses WHERE name = %s;",
            (course_name,)
        )
    
        # if course exists and course_id was found
        if row is not None:

            course_id = row[0]

            layout = db.fetch_one(
                "SELECT * FROM layouts WHERE name = %s AND course_id = %s;",
                (layout_name, course_id)
            )
            return layout
        
        return (None,)
    
    @classmethod
    def get_holes_in_layout_from_db(cls, db: DBManager, course_name: str, layout_name:str) -> tuple:

        layout_id = Layout.get_layout_info_from_db(db, course_name, layout_name)[0]

        if layout_id is not None:

            holes_in_layout = db.fetch_all(
                "SELECT * FROM holes_in_layouts WHERE layout_id = %s;",
                (layout_id,)
            )
            return holes_in_layout
        
        return (None,)




        
        # add all info to class attributes not return row


