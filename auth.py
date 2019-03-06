from db import *
from passlib.hash import argon2
import random
import string
import time

def check(sess):
    # code
    return False

def checkCred(usr, pwd):
    return argon2.verify(pwd, getPwdHash(usr))

def genSess():
    chars = string.ascii_letters + string.digits
    size = 16
    sess = ''.join(random.choice(chars) for i in range(size))
    # TODO: replace False with a check for whether or not the session ID is in use
    while(False):
        sess = ''.join(random.choice(chars) for i in range(size))
    # TODO: actually create the session somewhere in the DB
    return sess

def createUsr(usr, name, pwd):
    createRawUsr(usr, name, argon2.hash(pwd), time.time(), 0, usr)