from flask import Flask, request, redirect
from auth import *
from urls import *
app = Flask(__name__)

@app.route("/")
def home():
    return "6749"

@app.route("/ping")
def ping():
    return "pong"

@app.route("/login", methods=["GET", "POST"])
def login():
    if checkCred(request.values.get('usr', '\n'), request.values.get('pass', '\n')):
        return redirect(urls['login']['success'].replace('<SESS>', genSess()), code=302)
    else:
        return redirect(urls['login']['fail'], code=302)