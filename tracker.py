from flask import Flask, request
from auth import *
app = Flask(__name__)

@app.route("/")
def home():
    return "6749"

@app.route("/ping")
def ping():
    return "pong"

@app.route("/login", methods=["GET", "POST"])
def login():
    # TODO: make this redirect instead of returning a value
    if checkCred(request.values.get('usr'), request.values.get('pass')):
        return genSess()
    else:
        return "false"