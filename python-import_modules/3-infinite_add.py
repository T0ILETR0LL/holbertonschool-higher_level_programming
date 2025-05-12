#!/usr/bin/python3
from sys import argv
from calculator_1 import add

if __name__ == "__main__":
    length = len(argv) - 1
    if length == 0:
        print("0")
    if length == 1:
        print(f"{argv[1]}")
    if length >= 2:
        count = 1
        sum = int(argv[count])
        for count in range(1, length):
            sum = add(sum, int(argv[count+1]))
        print(f"{sum}")
