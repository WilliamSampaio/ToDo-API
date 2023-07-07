from typing import List

from fastapi import FastAPI, HTTPException

from data import ToDo
from models import ItemModel, ItemResponseModel

app = FastAPI()

todo = ToDo()


@app.get('/')
def hello():
    """
    Hello World!
    """
    return {'hello': 'world'}


@app.get('/todo', response_model=List[ItemResponseModel])
def list_todo():
    """
    List item.
    """
    return todo.list()


@app.post('/todo', response_model=ItemResponseModel, status_code=201)
def add_todo(item: ItemModel):
    """
    Add item.
    """
    return todo.add(dict(item))


@app.get('/{item_id}', response_model=ItemResponseModel)
def get_todo(item_id: int):
    """
    Get item.
    """
    item = todo.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return item
