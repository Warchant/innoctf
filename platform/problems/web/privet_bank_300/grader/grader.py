#!/bin/python

def grade(arg, key):
    if "InnoCTF{rounding_problem_is_still_alive_and_breathing}" == key:
        return True, "Right!"
    else:
        return False, "Hmm, maybe some other time?"
