import os
import logging
import sys
from flask import Flask, session,render_template,Response,request,redirect,url_for
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

app.secret_key = "any random string"


@app.route("/register")
def register():
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

@app.route("/admin")
def admin():
    Register=Registrations.query.all()
    return render_template("admin.html",regist=Register)

@app.route('/')
def index():
   if 'user' in session:
        user = session['user']
        return 'Logged in as ' + user + '<br>' + \
        "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'></b>" + \
    "click here to log in</b></a>"


@app.route("/auth",methods = ["GET","POST"])
def authenticate():
    Registrations.query.all()
    name = request.form.get("Fname")
    email = request.form.get("Email")
    log = Registrations(FIRSTNAME = name  ,EMAIL = email)
    try:
        Member = db.session.query(Registrations).filter(Registrations.EMAIL == email).all()
        print(Member[0].FIRSTNAME)
        session['user'] = request.form.get("Email")
        # return render_template("print.html",first=name,EMAIL = email)
        return redirect(url_for('index'))
    except Exception :
	    return render_template("error.html", errors = "Details are already given")       

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#    if request.method == 'POST':
      
#       return redirect(url_for('index1'))
#    return '''
	
#    <form action = "" method = "post">
#       <p><input type = text name = username/></p>
#       <p<<input type = submit value = Login/></p>
#    </form>
	
#    '''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('user', None)
   return redirect(url_for('register'))



    
        
 
    
