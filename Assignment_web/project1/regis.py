# sandhya
from flask_sqlalchemy import SQLAlchemy
from imports import *

db = SQLAlchemy()

class Registrations(db.Model):
    __tablename__ = "Registration"
    FIRSTNAME = db.Column(db.String, nullable=False)
    LASTNAME = db.Column(db.String, nullable=False)
    EMAIL = db.Column(db.String, primary_key=True)
    datetime =db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)

# db1 = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "BOOK"
    isbn = db.Column(db.String, nullable = False,primary_key=True)
    tittle = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.String, nullable= False)

# db.init_app(app)

# db1.create_all()



class Review(db.Model):
    __tablename__ = "reviews"
    # id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String, db.ForeignKey("Registration.EMAIL"))
    bookid = db.Column(db.String, db.ForeignKey("BOOKS.isbn"))
    text = db.Column(db.String, nullable = True)
    rating = db.Column(db.String, primary_key = True) 