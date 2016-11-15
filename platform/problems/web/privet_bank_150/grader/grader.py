#!/bin/python

def grade(arg, key):
    if "InnoCTF{csrf_exploitation_has_never_been_so_easy}" == key:
        return True, "Right!"
    else:
        return False, "Hmm, maybe some other time?"
