import random, string
import db

def getInfo(id: str):
    return db.getMatchInfo(id)

def genId() -> str:
    chars = string.ascii_letters + string.digits
    size: int = 32
    while(True):
        id: str = ''.join(random.choice(chars) for i in range(size))
        try:
            getInfo(id)
        except:
            return id

def add(team: int = 0, habStart: int = 1, ac: int = 0, ah: int = 0, tha: int = 0, thd: int = 0, thl: int = 0, thm: int = 0, thh: int = 0, tca: int = 0, tcd: int = 0, tcl: int = 0, tcm: int = 0, tch: int = 0, habEnd: int = 0, ct: float = 0, c: str = " "):
    c = " " if c == "" else c
    db.matchAdd(genId(), team, habStart, ac, ah, tha, thd, thl, thm, thh, tca, tcd, tcl, tcm, tch, habEnd, ct, c)
