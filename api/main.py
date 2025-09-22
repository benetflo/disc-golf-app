from fastapi import FastAPI
#import api.routes.db_manager as db
import uvicorn
from routes.db_manager import DBManager, init_tables

app = FastAPI()

@app.get("/home")
def read_root():
	return {"Hello": "World"}

if __name__ == "__main__":
	db = DBManager()
	init_tables(db)

	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
