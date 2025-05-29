#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    value = a_dictionary.get(key)
    if value is None:
        return a_dictionary
    a_dictionary.pop(key)
    return a_dictionary
