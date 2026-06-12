from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Store API", version="1.0.0")

books_db: dict[int, dict] = {}
next_id = 1


class Book(BaseModel):
    title: str
    author: str
    genre: str
    price: float
    stock: int
    published_year: int
    description: str | None = None


@app.get("/books/")
def list_books():
    return list(books_db.values())


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(404, "Book not found")
    return books_db[book_id]


@app.post("/books/", status_code=201)
def create_book(book: Book):
    global next_id
    entry = {"id": next_id, **book.model_dump()}
    books_db[next_id] = entry
    next_id += 1
    return entry


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if book_id not in books_db:
        raise HTTPException(404, "Book not found")
    entry = {"id": book_id, **book.model_dump()}
    books_db[book_id] = entry
    return entry


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(404, "Book not found")
    del books_db[book_id]
