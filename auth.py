from db import *
from passlib.hash import argon2
import random
import string
import time

def check(sess: str) -> bool:
    # code
    return False

def getPwdHash(usr: str) -> str:
    return getUsrInfo(usr)['hash']

def checkCred(usr: str, pwd: str) -> bool:
    return argon2.verify(pwd, getPwdHash(usr))

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
    createRawUsr(usr, name, argon2.hash(pwd), time.time(), 0, usr)

def grant(giver: str, getter: str, lvl: int):
    table.update_item(
        Key={
            'usr': getter
        },
        UpdateExpression="set lvl = :l, lastLvlChange: :c",
        ExpressionAttributeValues={
            ':l': lvl,
            ':c': upper
        }
    )

def createSess(usr: str, ip: str) -> str:
    sess: str = genSess()
    createRawSess(sess, usr, ip, time.time())
    return sess