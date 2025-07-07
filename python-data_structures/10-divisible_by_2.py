#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for val in my_list:
        if val % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result

#the new list (result) needs to be complete first by adding (appending) True or False in the same position as the values of my_list
#returning the result instead of True or False because we dont want to return just one element (it cant keep scanning alld values once returned)