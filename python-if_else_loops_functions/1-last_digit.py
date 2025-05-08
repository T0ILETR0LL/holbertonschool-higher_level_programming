#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10
if last_number == 0:
    sign = "and is 0"
if last_number > 5:
    sign = "and is greater than 5"
if last_number < 5:
    sign = "and is less than 5"
print(f"Last digit of {number} is {last_number} {sign}")
