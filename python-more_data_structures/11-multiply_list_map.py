#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    i = 0
    for value in my_list:
        new_list.append(value * number)
    return new_list