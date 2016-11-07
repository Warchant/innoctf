#!/bin/python

def grade(arg, key):
    if "InnoCTF{ppbmgjmk}" in key or "InnoCTF{ppbmgjkk}" in key:
        return True, "Correct!"
    else:
        return False, "Wrong answer, an example of flag is InnoCTF{abcdefgh}"
