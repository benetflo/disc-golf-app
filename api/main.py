from fastapi import FastAPI
import db_manager as db

app = FastAPI()

db = DBManager()

init_tables(db)


@app.get("/home")
def read_root():
	return {"Hello": "World"}
