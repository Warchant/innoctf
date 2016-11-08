#!/bin/python

def grade(arg, key):
    if "InnoCTF{was ist das}" == key:
        return True, "Nice! Proceed further"
    else:
        return False, "Ehm, how did you do that?"
