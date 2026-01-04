from fastapi import FastAPI

app = FastAPI()

@app.get("/{id}")
def root(id: int):
    return {"message": "Hello, FastAPI with ID {id}"}