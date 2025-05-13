#!/usr/bin/python3
def print_list_integer(my_list=[]):
    length = len(my_list) - 1
    for count in range(0, length+1):
        print("{}".format(my_list[count]))
