from fastapi import FastAPI
#import api.routes.db_manager as db
import uvicorn
from routes.db_manager import DBManager, init_tables
from routes.db_course_info import insert_new_layout, insert_new_course

app = FastAPI()

@app.get("/home")
def read_root():
	return {"Hello": "World"}

if __name__ == "__main__":
	db = DBManager()
	init_tables(db)
	#insert_new_course(db, "Rudan", "Stockholm - Haninge")
	insert_new_layout(db, "Rudan", "Full", "Standard 18 hole layout")

	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
