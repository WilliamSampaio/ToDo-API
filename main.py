from fastapi import FastAPI
from typing import List
from data import ToDo
from models import ItemModel

app = FastAPI()

todo = ToDo()


@app.get('/')
def hello():
    """
    Hello World!
    """
    return {'hello': 'world'}


@app.get('/todo', response_model=List[ItemModel])
def list_todo():
    """
    List item.
    """
    return todo.list()


@app.post('/todo', response_model=ItemModel, status_code=201)
def add_todo(item: ItemModel):
    """
    Add item.
    """
    return todo.add(dict(item))
