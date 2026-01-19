from fastapi import APIRouter , HTTPException
from schemas import Book
router = APIRouter()

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


@router.get("/books/search")
async def search_books(genre : str , pages : int | None = None ):
    return {
        "genre" : genre ,
        "pages" : pages
    }
@router.get("/books/{book_id}")
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



@router.post("/book")
async def create_book(book : Book):
    book_data =  book.model_dump()
    books_db.append(book_data)
    return {
        "message" : "Book added successfully" ,
        "book_details" : book_data ,
        "entire_books_database" : books_db
    }



## PUT
@router.put("/books/{book_id}")
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


@router.delete("/books/{book_id}")
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


