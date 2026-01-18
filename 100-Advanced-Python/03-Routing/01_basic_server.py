"""
The Library System

Task: Write a FastAPI app with two endpoints.

1. Get Book by ID (Path Parameter):
    Path: /books/{book_id}
    Logic: Return a dictionary {"book_id": book_id, "title": "The Great Gatsby"}.
    Constraint: Ensure book_id is an integer.
2. Search Books (Query Parameters):
    Path: /books/search
    Logic: Accept a parameter genre (str) and pages (int).
    Return: {"genre": genre, "pages": pages}.
    Constraint: Make pages optional (default to None) using the int | None = None syntax you learned.

Write the code for these two endpoints! ✍️
"""

from fastapi import FastAPI
from pydantic import BaseModel , Field
app = FastAPI()

@app.get("/")
async def health_check():
    return {
        "message" : "Health is fine!"
    }
# In-memory database
books_db = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "price": 399
    },
    {
        "id": 2,
        "title": "Deep Work",
        "author": "Cal Newport",
        "price": 499
    }
]

@app.get("/books/search")
async def search_books(genre : str , pages : int | None = None ):
    return {
        "genre" : genre ,
        "pages" : pages
    }
@app.get("/books/{book_id}")
async def get_books(book_id : int) :
    """
    Description :
    Get Book by ID (Path Parameter):
        Path: /books/{book_id}
        Logic: Return a dictionary {"book_id": book_id, "title": "The Great Gatsby"}.
        Constraint: Ensure book_id is an integer.
    Args:
        book_id:
    Returns:
        dictionary of the book
    """

    for book in books_db:
        if book["id"] == book_id:
            return book
    return {
        "message" : "Book not found!"
    }


