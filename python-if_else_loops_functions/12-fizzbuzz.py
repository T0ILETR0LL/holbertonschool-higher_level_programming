#!/usr/bin/python3
def fizzbuzz():
    for count in range(1, 101):
        if (count % 3) == 0:
            if (count % 5) == 0:
                print("FizzBuzz", end=" ")
            else:
                print("Fizz", end=" ")
        elif (count % 5) == 0:
            print("Buzz", end=" ")
        else:
            print(count, end=" ")
