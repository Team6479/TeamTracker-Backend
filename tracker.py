from flask import Flask, request, redirect
import auth
import match
import pit
from urls import urls
app = Flask(__name__)

@app.route("/")
def home():
    return "6749"

@app.route("/ping")
def ping():
    return "pong"

@app.route("/user/login", methods=["GET", "POST"])
def login():
    if auth.checkCred(request.values.get('usr', '\n'), request.values.get('pass', '\n')):
        return redirect(urls['login']['success'].replace('<SESS>', auth.createSess(request.values.get('usr', '\n'), request.remote_addr)), code=302)
    else:
        return redirect(urls['login']['fail'], code=302)

@app.route("/user/logout", methods=["GET", "POST"])
def logout():
    if auth.check(request.values.get('sess', '\n')):
        auth.rmSess(request.values.get('sess', '\n'))
        return redirect(urls['login']['page'], code=302)
    else:
        return redirect(urls['login']['fail'], code=302)

@app.route("/user/check", methods=["GET", "POST"])
def check():
    if auth.check(request.values.get('sess', '\n')):
        return str(auth.getLvl(auth.getUsrFromSess(request.values.get('sess', '\n'))))
    else:
        return "0"

@app.route("/user/grant", methods=["GET", "POST"])
def grant():
    if auth.check(request.values.get('sess', '\n')):
        lvl: int = auth.getLvl(auth.getUsrFromSess(request.values.get('sess', '\n')))
        if request.values.get((request.values.get('lvl', '\n', int), 0)):
            auth.grant() # TODO: write some code
    else:
        return redirect(urls['login']['invalid'], code=302)