from fastapi import FastAPI


app = FastAPI()


BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/")
async def home():
    return {"message": "Hello World!"}


@app.get("/books")
async def get_books():
    return BOOKS


@app.get("/books/title/{title}")
async def get_book_by_id(title: str):
    for book in BOOKS:
        if book["title"].lower() == title.lower():
            return book


@app.get("/books/")
async def get_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book["category"] == category:
            books_to_return.append(book)

    return books_to_return


@app.get("/books/author/{author}")
async def get_books_by_author(author: str):
    author_books = []
    for book in BOOKS:
        if book["author"].lower() == author.lower():
            author_books.append(book)
    
    return author_books

