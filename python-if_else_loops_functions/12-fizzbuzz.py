#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end=" ")
        else:
            if i % 5 == 0:
                print("Buzz", end=" ")
            else:
                if i % 3 == 0:
                    print("Fizz", end=" ")
                else:
                    print(i, end=" ")
