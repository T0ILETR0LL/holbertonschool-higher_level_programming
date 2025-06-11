#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divide = a/b
        print("Inside result:")
        return divide
    except:
        print("Inside result: None")
        return None