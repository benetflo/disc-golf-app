from fastapi import FastAPI
#import api.routes.db_manager as db
#import db_manager as db
from api.routes.db_manager import DBManager, init_tables

app = FastAPI()

db = DBManager()



@app.get("/home")
def read_root():
	return {"Hello": "World"}

if __name__ == "__main__":
	db = DBManager()
	init_tables(db)