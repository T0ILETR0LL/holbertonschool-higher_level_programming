#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary.items())
    for keys, value in new:
        print(f"{keys}: {value}")
