#!/bin/python

def grade(arg, key):
    if "InnoCTF{banana}" == key:
        return True, "Correct!"
	elif "InnoCTF{flagisbanana}" == key:
        return True, "Correct!"
    else:
        return False, "Wrong answer :("
