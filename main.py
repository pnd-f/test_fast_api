from fastapi import FastAPI
from pydantic import BaseModel
from os import getenv

my_app = FastAPI()


class Book(BaseModel):
    title: str
    price: float
    is_offer: bool | None = None


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


@my_app.post("/envvars/")
async def get_env_vars():
    env_vars = {
        'postgres': getenv('POSTGRES_CONNECTION'),
        'mongo': getenv('MONGODB_CONNECTION'),
        'redis': getenv('REDIS_CONNECTION'),
    }
    return env_vars
