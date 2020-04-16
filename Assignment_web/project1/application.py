import os
import logging
import sys
from flask import Flask, session,render_template,Response,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from regis import *
from datetime import datetime

# 


   

app = Flask(__name__)
# db=SQLAlchemy(app)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Session(app)

# Set up database

# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))
db.init_app(app)




@app.route("/")
def index():
    return render_template("Registration.html")

@app.route("/print",methods=["POST","GET"])
def print1():
    Registrations.query.all()
    first = request.form.get("Fname")
    last = request.form.get("Lname")
    email = request.form.get("Email")
    regist = Registrations(FIRSTNAME=first, LASTNAME=last,EMAIL=email,datetime=datetime.now())
    try:
        db.session.add(regist)
        db.session.commit()
        print(first+" "+email)
        return render_template("print.html",first=first,EMAIL = email)
    except Exception :
	    return render_template("error.html", errors = "Details are already given")


    
        
 
    
