import os
import logging
import sys
from flask import Flask, session,render_template,Response,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("Registration.html")

@app.route("/print",methods=["POST","GET"])
def print1():
    first=request.form.get("Fname")
    last=request.form.get("Lname")
    print(first,last)
    return render_template("print.html",first=first,last=last)
    
