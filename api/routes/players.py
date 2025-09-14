import db_manager as db

def register_new_player(db, name):
    db.execute(
        "INSERT INTO players (name) VALUES (%s);",
        (name,)  # kommatecknet är viktigt för att det ska vara en tuple
    )