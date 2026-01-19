from pydantic import BaseModel 
#
# id: int
# title: str
# author: str
# price: float

class Book(BaseModel):
    id : int
    title : str
    author : str
    price : float



