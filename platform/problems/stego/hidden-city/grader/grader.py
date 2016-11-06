#!/bin/python

def grade(arg, key):
    if "InnoCTF{London}" == key:
        return True, "Correct!"
    else:
        return False, "Wrong answer, an example of flag is InnoCTF{Kazan}"
