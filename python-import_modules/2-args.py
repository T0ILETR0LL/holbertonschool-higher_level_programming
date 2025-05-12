#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
    if length == 1:
        print("1 argument: ")
        print(f"1: {argv[1]}")
    if length >= 2:
        count = 1
        print(f"{length} arguments:")
        for count in range(1, length + 1):
            print(f"{count}: {argv[count]}")