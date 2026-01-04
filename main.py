from fastapi import FastAPI

app = FastAPI()

@app.get("/{id}")
def root(id: int):
    return {"message": f"Hello, FastAPI with ID {id}"}

@app.post("/todo")
def create_todo(item: dict):
    return {"message": "Todo created", "item": item}