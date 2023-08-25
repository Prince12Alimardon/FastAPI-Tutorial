from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
async def hello():
    return {'text': 'FastAPI tutorial course'}


@app.get('/books/{book_id}')  # path parameter
async def get_book(book_id: int):
    return {'book_id': book_id}


@app.get('/books')  # query paramet
async def read_books(number: int, text: Optional[str]):
    return {'number': number, 'text': text}
