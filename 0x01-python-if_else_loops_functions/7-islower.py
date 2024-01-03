#!/usr/bin/python3
def islower(c):
    if type(c) == "<class 'int'>":
        return False
    elif c == c.lower():
        return True
    else:
        return False
