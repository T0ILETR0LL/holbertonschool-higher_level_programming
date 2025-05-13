#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list) - 1
    if idx <= -1:
        return my_list
    if idx >= length + 1:
        return my_list
    else:
        new_list = my_list
        my_list[idx] = element
        return new_list