#!/bin/python

def grade(arg, key):
    if "InnoCTF{3xp@nd_th3_br0ws3r}" == key:
        return True, "Right!"
    else:
        return False, "Hmm, maybe some other time?"
