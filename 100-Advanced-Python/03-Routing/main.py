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
from pyexpat.errors import messages

from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
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
    raise HTTPException(status_code=404 , detail="Book not found")

## POST Request to create a new book
## BODY Pydantic Model
# In FastAPI -- we send all the things like body and all in the function paramaters itself -- it is there
class Book(BaseModel):
    id : int
    title : str
    author : str
    price : float


@app.post("/book")
async def create_book(book : Book):
    book_data =  book.model_dump()
    books_db.append(book_data)
    return {
        "message" : "Book added successfully" ,
        "book_details" : book_data ,
        "entire_books_database" : books_db
    }



## PUT
@app.put("/books/{book_id}")
async def update_book(book_id : int , updated_book_data : Book) :
    for index , book in enumerate(books_db):
        if book["id"] == book_id :
            book.update(updated_book_data.model_dump())

            return {
                "message": "The book has been updated.",
                "updated_book": updated_book_data,
                "entire_database": books_db
            }
    return {
        "message":"Book not found!" ,
        "find_books_below" : books_db
    }


@app.delete("/books/{book_id}")
async def delete_book(book_id : int):
    for index , book in enumerate(books_db):
        if book["id"] == book_id :
            books_db.pop(index)
            return {
                "message" : "Book removed" ,
                "books_removed" : book
            }
    return {
        "Message" : "Book not found!"
    }


