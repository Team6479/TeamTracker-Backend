from flask import Flask
from auth import *
app = Flask(__name__)

@app.route("/")
def home():
    return "6749"

@app.route("/ping")
def ping():
    return "pong"

@app.route("/<sess>")
def checkSess(sess):
    return check(sess)