from fastapi import FastAPI
#import api.routes.db_manager as db
import uvicorn
from db_operations.db_manager import DBManager
from db_operations.player import Player
from db_operations.db_init_tables import init_tables


app = FastAPI()

@app.get("/home")
def read_root():
	return {"Hello": "World"}

if __name__ == "__main__":
	db = DBManager()
	init_tables(db)

	a = Player("Simon B", "Cuddlew")

	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
