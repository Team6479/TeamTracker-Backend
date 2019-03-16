from flask import Flask, request, redirect
import json

import util
import auth
import match
import pit
from urls import urls

app = Flask(__name__)

# General utilities that don't access any databases (these should not rely on any other files)
@app.route("/")
def home():
    return "6749"

@app.route("/ping")
def ping():
    return "pong"

# User-related endpoints (these should only rely on auth.py, util.py, and urls.py)
@app.route("/user/login", methods=["GET", "POST"])
def user_login(): # redir
    if not util.reqIsCleanPwd(request.values, request.values.get('pass', '\n')):
        return redirect(urls['input']['illegal']['chars'], code=302)
    if auth.checkCred(request.values.get('usr', '\n'), request.values.get('pass', '\n')):
        return redirect(urls['login']['success'].replace('<SESS>', auth.createSess(request.values.get('usr', '\n'), request.remote_addr)), code=302)
    else:
        return redirect(urls['login']['fail'], code=302)

@app.route("/user/logout", methods=["GET", "POST"])
def user_logout(): # redir
    if not util.reqIsClean(request.values):
        return redirect(urls['input']['illegal']['chars'], code=302)
    if auth.check(request.values.get('sess', '\n')):
        auth.rmSess(request.values.get('sess', '\n'))
        return redirect(urls['login']['page'], code=302)
    else:
        return redirect(urls['login']['fail'], code=302)

@app.route("/user/check", methods=["GET", "POST"])
def user_check(): # int
    if not util.reqIsClean(request.values):
        return redirect(urls['input']['illegal']['chars'], code=302)
    if auth.check(request.values.get('sess', '\n')):
        return str(auth.getLvl(auth.getUsrFromSess(request.values.get('sess', '\n'))))
    else:
        return "0"

@app.route("/user/grant", methods=["GET", "POST"])
def user_grant(): # redir
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
def user_create(): # redir
    if not util.reqIsCleanPwd(request.values, request.values.get('pass', '\n')):
        return redirect(urls['input']['illegal']['chars'], code=302)
    if request.values.get('sess', '\n') == '\n':
        if request.values.get('usr', '\n') == '\n':
            return redirect(urls['input']['illegal']['absent'], code=302)
        else:
            auth.createUsr(request.values.get('usr', '\n'), request.values.get('name', '\n'), request.values.get('pass', '\n'))
            return redirect(urls['login']['created'], code=302)
    else:
        return redirect(urls['login']['why'], code=302)

@app.route("/user", methods=["GET", "POST"]) # Stack Overflow says this works
@app.route("/user/info", methods=["GET", "POST"]) # /user acts as an alias for /user/info
def user_info(): # json
    if request.values.get('sess', '\n') == '\n': # the user must be logged in to view user info, but they don't necessarily need any permissions
        if request.values.get('usr', '\n') == '\n': # if no user is supplied, get the info from the user who is logged in according to the session
            usr = auth.getUsrFromSess(request.values.get('sess', '\n'))
        else: # if the caller supplied a usr param, get that user's info
            usr = request.values.get('usr', '\n')
    else: # if the user isn't logged in, get the info for the user invalid
        usr = 'invalid'
    return json.dumps(auth.getUsrInfo(usr))

# Accessing data (these should use everything except for db.py)
# TODO: write code

# Writing data (these should use everything except for db.py)
# TODO: write code