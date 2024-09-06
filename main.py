from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from datetime import datetime

holiday = datetime(year=2023, month=11, day=6)
today = datetime.today()
if today.month == holiday.month and \
        today.day == holiday.day:
    print('У вас выходной!')

my_app = FastAPI()


class Book(BaseModel):
    title: str
    price: float
    is_offer: Union[bool, None] = None


@my_app.get("/")
def just_say_hello():
    return {"Hello": "World"}


@my_app.get("/books/{book_id}")
def read_book(book_id: int, q: str | None = None):
    return {"book_id": book_id, "q": q}


@my_app.patch("/books/{book_id}")
def update_book(book_id: int, book: Book | None = None):
    return {"book_name": book.title, "book_id": book_id}


@my_app.post("/books/")
async def create_book(book: Book):
    return book
