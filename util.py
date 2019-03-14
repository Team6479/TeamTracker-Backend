import re

def isClean(s: str) -> bool:
    return bool(re.match('^[a-zA-Z0-9_]+$', s))
def reqIsClean(r) -> bool:
    for x in r:
        if not isClean(x):
            return False
    return True