# sandhya
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Registrations(db.Model):
    __tablename__ = "Registration"
    FIRSTNAME = db.Column(db.String, nullable=False)
    LASTNAME = db.Column(db.String, nullable=False)
    EMAIL = db.Column(db.String, primary_key=True)
    datetime =db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)
      