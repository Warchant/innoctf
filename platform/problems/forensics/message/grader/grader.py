#!/bin/python

def grade(arg, key):
    if "InnoCTF{banana}" == key:
        return True, "Флаг принят"
	elif "InnoCTF{flagisbanana}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
