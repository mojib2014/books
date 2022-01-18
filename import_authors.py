import csv
import os
from sqlite3 import IntegrityError

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)

def main():
    file = open("books.csv")
    reader = csv.reader(file)
    authors = set()
    for col in reader:
       authors.add(col[2])
       
    for author in authors:
        author = Author(name=author)
        db.session.add(author)
        print(f"{author} Added to the database.")

    db.session.commit()

if __name__ == "__main__":
    main()