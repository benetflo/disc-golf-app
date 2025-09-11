from fastapi import FastAPI

app = FastAPI()

# koppla till databas


@app.get("/home")
def read_root():
	return {"Hello": "World"}
