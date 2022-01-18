import os 

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query").title()
    books = Book.query.filter(Book.title.like("%{}%".format(query))).all()
    authors = Author.query.filter(Author.name.like("%{}%".format(query))).all()
    if books is None or authors is None:
        return render_template("error.html", message=f"No books or authors for query {query}")

    return render_template("books.html", books=books, authors=authors, query=query)

@app.route("/books/<int:book_id>")
def books(book_id):
    book = Book.query.get(book_id)
    author = Author.query.get(book.author_id)
    if book is None:
        return render_template("error.html", message="Book with the given ID was not found!")
   
    return render_template("book_detail.html", book=book, author=author)
    
@app.route("/authors/<int:author_id>")
def authors(author_id):
    author = Author.query.get(author_id)
    if author is None:
        return render_template("error.html", message="Author with the given ID was not found!")
    
    return render_template("author_detail.html", author=author)

if __name__ == "__main__":
    app.run(debug=True)