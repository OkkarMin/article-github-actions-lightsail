from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/{item_id}")
def create_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# q: how to use sed to replace : with -
# sed -i 's/:/-/g' main.py
