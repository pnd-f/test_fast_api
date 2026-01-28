from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from os import getenv, environ

my_app = FastAPI()

# Configure CORS
my_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@my_app.get("/envvars/")
async def get_env_vars():
    env_vars = {
        'postgres': getenv('POSTGRES_CONNECTION'),
        'mongo': getenv('MONGODB_CONNECTION'),
        'redis': getenv('REDIS_CONNECTION'),
        'all': environ
    }
    return env_vars
