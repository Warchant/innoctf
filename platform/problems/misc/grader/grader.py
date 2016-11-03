#!/bin/python

def grade(arg, key):
    if "InnoCTF{l3ts_pl4y_th3_g4m3}" == key:
        return True, "Nice! Proceed further"
    else:
        return False, "Ehm, how did you do that?"
