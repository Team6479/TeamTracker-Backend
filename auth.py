import db
from passlib.hash import argon2
import random
import string
import time

def getIpFromSess(sess: str) -> str:
    return db.getSessInfo(sess)['ip']

def check(sess: str, ip: str = '\n') -> bool:
    try:
        db.getSessInfo(sess)
        if ip == '\n':
            return True
        else:
            return ip == getIpFromSess(sess)
    except:
        return False
    return False
def getUsrFromSess(sess: str) -> str:
    return db.getSessInfo(sess)['usr']

def getUsrInfo(usr: str):
    return db.getUsrInfo(usr)
def getPwdHash(usr: str) -> str:
    return getUsrInfo(usr)['hash']
def getLvl(usr: str) -> int:
    return getUsrInfo(usr)['lvl']

def checkCred(usr: str, pwd: str) -> bool:
    try:
        res = argon2.verify(pwd, getPwdHash(usr))
        if not res:
            time.sleep(0.5)
        return res
    except:
        time.sleep(0.5)
        return False

def genSess() -> str:
    chars = string.ascii_letters + string.digits
    size: int = 16
    sess: str = ''.join(random.choice(chars) for i in range(size))
    # TODO: replace False with a check for whether or not the session ID is in use
    while(False):
        sess = ''.join(random.choice(chars) for i in range(size))
    # TODO: actually create the session somewhere in the DB
    return sess

def createUsr(usr: str, name: str, pwd: str):
    db.createRawUsr(usr, name, argon2.hash(pwd), time.time(), 0, usr)

def createSess(usr: str, ip: str) -> str:
    sess: str = genSess()
    db.createRawSess(sess, usr, ip, time.time())
    return sess

def rmSess(sess: str):
    db.rmSess(sess)

def grant(giver: str, getter: str, lvl: int):
    db.grant(giver, getter, lvl)