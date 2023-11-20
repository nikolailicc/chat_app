from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
    
class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int



BOOKS = [
    Book(1,"computer science","Djuka","Knjiga vrh",10),
    Book(2,"biJologija","Milica","stas",3),
    Book(3,"masinstvo","Boban","alkohol",0)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create/book")
async def create_book(book_request: BookRequest):
    newBook = Book(**book_request.model_dump())
    BOOKS.append(newBook)