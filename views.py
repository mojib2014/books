from app import app
from flask import render_template, request
from models import *

QUERY = ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    QUERY = request.form.get("query").title()
    books = Book.query.filter_by(title=QUERY).all()
    print(f"books books books: {books}")
    authors = Author.query.filter_by(name=QUERY).all()
    if books is None or authors is None:
        return render_template("error.html", message=f"No books or authors for query {QUERY}")

    return render_template("books.html", books=books, authors=authors, query=QUERY)

@app.route("/books/<int:book_id>")
def books(book_id):
    book = Book.query.get(book_id)
    author = Author.query.get(book.author_id)
    if book is None:
        return render_template("error.html", message="Book with the given ID was not found!")

    return render_template("book_detail.html", book=book, author=author, query=QUERY)
    
@app.route("/authors/<int:author_id>")
def authors(author_id):
    author = Author.query.get(author_id)
    if author is None:
        return render_template("error.html", message="Author with the given ID was not found!")
    
    return render_template("author_detail.html", author=author, query=QUERY)