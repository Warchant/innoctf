#!/bin/python

def grade(arg, key):
    if "InnoCTF{csrf_exploitation_has_never_been_so_easy}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
