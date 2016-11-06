#!/bin/python

def grade(arg, key):
    if "InnoCTF{Win32.Trojaner.DeutschePorno}" == key:
        return True, "Nice! Proceed further"
    else:
        return False, "Ehm, how did you do that?"
