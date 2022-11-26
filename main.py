from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "Greetings from FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/{item_id}")
def create_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
