#!/bin/python

def grade(arg, key):
    if "InnoCTF{L3T_M3_M0RE}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
