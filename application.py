# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def print_rollno():
  return "Roll No : 2306"
  
