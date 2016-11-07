#!/bin/python

def grade(arg, key):
    if "InnoCTF{sngwwlsik}" in key or "InnoCTF{sngwwlsic}" in key:
        return True, "Correct!"
    else:
        return False, "Wrong answer, an example of flag is InnoCTF{abcdefghi}"
