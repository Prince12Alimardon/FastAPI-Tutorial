from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI(title='Todo APP')


class Todo(BaseModel):
    name: str
    description: Optional[str] = None


# create, read, update, delete
storage = []


@app.post('/todo')
async def post(todo: Todo):
    storage.append(todo)
    return todo


@app.get('/todo/', response_model=list[Todo])
async def get_all_todos():
    return storage


@app.get('/todo/{id}')
async def get_one_todo(id: int):
    try:
        return storage[id]
    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')


@app.put('/todo/{id}')
async def update(id: int, todo: Todo):
    try:
        storage[id] = todo
        return storage[id]
    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')


@app.delete('/todo/{id}')
async def delete(id: int):
    try:
        obj = storage[id]
        storage.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')
