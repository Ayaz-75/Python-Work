from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class DirectionName(str, Enum):
    noth = "North"
    south = "South"
    east = "East"
    west = "West"


BOOKS = {
    "book_1": {"title": "title 1", "name": "Book 1", "author": "author 1"},
    "book_2": {"title": "title 2", "name": "Book 2", "author": "author 2"},
    "book_3": {"title": "title 3", "name": "Book 3", "author": "author 3"},
    "book_4": {"title": "title 4", "name": "Book 4", "author": "author 4"},
    "book_5": {"title": "title 5", "name": "Book 5", "author": "author 5"},
}



@app.get("/")
async def first_api():
    return {"message": "Hey Ayaz!!!"}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title):
    return {"book_title": book_title}

@app.get("/books/{book_id}")
async def read_book_id(book_id: int):
    return {"book_id": book_id}


@app.get("directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.noth:
        return {"direction": "Up"}
    if direction_name == DirectionName.south:
        return {"direction": "Down"}
    if direction_name == DirectionName.east:
        return {"direction": "Left"}
    if direction_name == DirectionName.west:
        return {"direction": "Right"}


@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]

