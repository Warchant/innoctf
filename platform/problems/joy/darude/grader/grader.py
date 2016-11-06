#!/bin/python

def grade(arg, key):
    if "InnoCTF{sngwwlsik}" == key:
        return True, "Correct!"
	elif "InnoCTF{sngwwlsic}" == key:
		return True, "Correct!"
    else:
        return False, "Wrong answer, an example of flag is InnoCTF{abcdefghi}"
