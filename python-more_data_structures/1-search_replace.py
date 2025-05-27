#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_list = my_list [:]
    i = 0
    for value in my_list:
        if my_list[i] == search:
            replace_list[i] = replace
        i += 1
    return replace_list