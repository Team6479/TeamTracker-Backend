from flask import Flask, request, redirect
import util
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
    if not util.reqIsClean(request.values):
        return redirect(urls['input']['illegal']['chars'], code=302)
    if auth.checkCred(request.values.get('usr', '\n'), request.values.get('pass', '\n')):
        return redirect(urls['login']['success'].replace('<SESS>', auth.createSess(request.values.get('usr', '\n'), request.remote_addr)), code=302)
    else:
        return redirect(urls['login']['fail'], code=302)

@app.route("/user/logout", methods=["GET", "POST"])
def logout():
    if not util.reqIsClean(request.values):
        return redirect(urls['input']['illegal']['chars'], code=302)
    if auth.check(request.values.get('sess', '\n')):
        auth.rmSess(request.values.get('sess', '\n'))
        return redirect(urls['login']['page'], code=302)
    else:
        return redirect(urls['login']['fail'], code=302)

@app.route("/user/check", methods=["GET", "POST"])
def check():
    if not util.reqIsClean(request.values):
        return redirect(urls['input']['illegal']['chars'], code=302)
    if auth.check(request.values.get('sess', '\n')):
        return str(auth.getLvl(auth.getUsrFromSess(request.values.get('sess', '\n'))))
    else:
        return "0"

@app.route("/user/grant", methods=["GET", "POST"])
def grant():
    if not util.reqIsClean(request.values):
        return redirect(urls['input']['illegal']['chars'], code=302)
    if auth.check(request.values.get('sess', '\n')):
        lvl: int = auth.getLvl(auth.getUsrFromSess(request.values.get('sess', '\n')))
        if (request.values.get('lvl', 0, int) < lvl or request.values.get('lvl', 0, int) == 0):
            auth.grant(auth.getUsrFromSess(request.values.get('sess', '\n')), request.values.get('usr', '\n'), request.values.get('lvl', 0, int))
            return redirect(urls['login']['granted'], code=302)
        else:
            return redirect(urls['login']['invalid'], code=302)
    else:
        return redirect(urls['login']['invalid'], code=302)

@app.route("/user/create", methods=["GET", "POST"])
def create():
    if not util.reqIsClean(request.values):
        return redirect(urls['input']['illegal']['chars'], code=302)
    if request.values.get('sess', '\n') == '\n':
        if request.values.get('usr', '\n') == '\n':
            return redirect(urls['input']['illegal']['absent'], code=302)
        else:
            auth.createUsr(request.values.get('usr', '\n'), request.values.get('name', '\n'), request.values.get('pass', '\n'))
            return redirect(urls['login']['created'], code=302)
    else:
        return redirect(urls['login']['why'], code=302)