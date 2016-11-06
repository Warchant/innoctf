#!/bin/python

def grade(arg, key):
    if "InnoCTF{y0u_w1n_us3_RCE_1n_my5QL}" == key:
        return True, "Right!"
    else:
        return False, "Hmm, maybe some other time?"
