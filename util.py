import re

def isClean(s: str) -> bool: # Accept only alphanumeric characters and underscores
    return bool(re.match('^[a-zA-Z0-9_]+$', s))
def isPwdClean(s: str) -> bool: # Accept only alphanumeric characters and most non-hackery symbols (and also newlines so that the errors are good)
    return bool(re.match('[a-zA-Z0-9!@#$%^&*()_\\-=+/,.\\\\|\n]+$', s))
def reqIsClean(r) -> bool:
    for x in r:
        if not isClean(x):
            return False
    return True
def reqIsCleanPwd(r, pwd: str) -> bool:
    for x in r:
        if not isClean(x) and x != pwd:
            return False
    return True