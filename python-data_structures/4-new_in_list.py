#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    length = len(my_list) - 1
    if idx <= -1:
        return my_list
    if idx >= length + 1:
        return my_list
    else:
        list_copy = my_list[:]
        list_copy[idx] = new_element
        return list_copy