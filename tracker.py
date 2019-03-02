from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "6749"

@app.route("/ping")
def ping():
    return "pong"