#!/bin/python

def grade(arg, key):
    if "InnoCTF{f@cT0R-ma$73r!}" == key:
        return True, "+"
    else:
        return False, "-"
