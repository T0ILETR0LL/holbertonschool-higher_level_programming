#!/usr/bin/python3
my_string = "Best SchoCol"

new_string = ""

for c in my_string:
    if c != 'c' and c != 'C':
        print(c, end="")
        new_string = new_string + c

print()
print(new_string)