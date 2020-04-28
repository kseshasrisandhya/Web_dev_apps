#  sandhya
import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from models import Book
from sqlalchemy import Column, Integer, String,DateTime,exists,Sequence
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from regis import *


# Import table definitions.

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.app_context().push()
# Link the Flask app1 with the database (no Flask app1 is actually being run yet).     

db = SQLAlchemy()

# class Books(db1.Model):
#     __tablename__ = "BOOKS"
#     isbn = db1.Column(db1.String, nullable = False,primary_key=True)
#     tittle = db1.Column(db1.String, nullable = False)
#     author = db1.Column(db1.String, nullable = False)
#     year = db1.Column(db1.String, nullable= False)

db.init_app(app)

db.create_all()
def main():
    f= open("books.csv")
    reader = csv.reader(f)
    for isbn, tittle, author, year in reader:
        book = Book(isbn= isbn, tittle=tittle, author=author, year=year)
        db.session.add(book)
    db.session.commit()

if __name__ == "__main__":
    main()


