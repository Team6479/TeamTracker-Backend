from db import *
from passlib.hash import argon2
from random import choice
import string

def check(sess):
    # code
    return False

def checkCred(usr, pwd):
    return argon2.verify(pswd, getPwdHash(usr))

def genSess(usr):
    chars = string.ascii_letters + string.digits
    size = 16
    sess = ''.join(random.choice(chars) for i in range(size))
    # TODO: replace False with a check for whether or not the session ID is in use
    while(False):
        sess = ''.join(random.choice(chars) for i in range(size))
    # TODO: actually create the session somewhere in the DB
    return sess