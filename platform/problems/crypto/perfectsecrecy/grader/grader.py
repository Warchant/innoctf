#!/bin/python

def grade(arg, key):
    if "InnoCTF{xorcipherisnotsecure}" in key:
        return True, "Unglaublich!"
    else:
        return False, "Schießen!"
