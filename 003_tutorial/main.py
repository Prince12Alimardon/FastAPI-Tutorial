from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    name: str
    author: str
    price: int
    description: Optional[str] = None


# @app.post('/books')
# async def post_book(books: Book):
#     return books


@app.post('/books/{priority}')
async def create_books(priority: int, book: Book, value: bool):
    return {
        'priority': priority,
        **book.dict(),
        'value': value,
    }
