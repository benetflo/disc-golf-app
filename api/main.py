from fastapi import FastAPI, HTTPException
#import api.routes.db_manager as db
import uvicorn
from db_operations.db_manager import DBManager
from db_operations.player import Player
from db_operations.course import Course
from db_operations.layout import Layout
from db_operations.hole import Hole
from db_operations.db_init_tables import init_tables

app = FastAPI()
db = DBManager()


@app.get("/players/{username}")
def get_player_info(username: str):
	
	player = Player.get_player_info_from_db(db, username)
	
	if player is None:
		raise HTTPException(status_code=404, detail="Player not found")
		
	return {"player": player}

@app.get("/courses/{name}")
def get_course_info(name: str):

	course = Course.get_course_info_from_db(db, name)

	if course is None:
		raise HTTPException(status_code=404, detail="Course not found")

	return {"course": course}

@app.get("/layouts/{course_name}/{layout_name}")
def get_layout_info(course_name: str, layout_name: str):

	layout = Layout.get_layout_info_from_db(db, course_name, layout_name)

	if layout is None:
		raise HTTPException(status_code=404, detail="Layout not found")

	return {"layout": layout}

@app.get("/holes_in_layouts/{course_name}/{layout_name}")
def get_holes_in_layouts_info(course_name: str, layout_name: str):
	holes_in_layout = Layout.get_holes_in_layout_from_db(db, course_name, layout_name)
	
	if holes_in_layout is None:
		raise HTTPException(status_code=404, detail="Layout not found")
	
	return {f"holes_in_layout {layout_name}": holes_in_layout}


@app.get("/holes/{course_name}")
def get_holes_in_course_info(course_name: str):

	holes = Hole.get_holes_in_course_info_from_db(db, course_name)

	return {f"{course_name} holes": holes}




	
if __name__ == "__main__":
	init_tables(db)

	a = Course("Rudan", "Haninge")
	a.insert_new_course_to_db(db)

	d = Layout("Rudan", "Monstret", "Main 18 holes")
	d.insert_layout_to_db(db)

	b = Hole(85, 3, "Fuck off")
	b.insert_hole_to_db(db, "Rudan", "Monstret", 1)

#	c = Hole(40, 5, "Easy")
#	c.insert_new_hole(db, "Rudan")

#	e = Hole(40, 5, "Easy")
#	e.insert_new_hole(db, "Tyresö")

	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)