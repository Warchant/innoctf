#!/bin/python

def grade(arg, key):
    if "InnoCTF{1ph0ne7_w45_5ucc35fu11y_b0u6h7}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
