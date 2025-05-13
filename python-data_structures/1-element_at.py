#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list) - 1
    if idx <= -1:
        return None
    if idx >= length + 1:
        return None
    else:
        return my_list[idx]
