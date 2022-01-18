import csv
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)

def main():
    file = open("books.csv")
    reader = csv.reader(file)
    authors = Author.query.all()
    for isbn, title, author, year in reader:
        for autor in authors:
            if author == autor.name:
                book = Book(isbn=isbn, title=title, year=year, author_id=autor.id)
                db.session.add(book)
                print(f"{isbn}, {title}, {year} inserted into books")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()