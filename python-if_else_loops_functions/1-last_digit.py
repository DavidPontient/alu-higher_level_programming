#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = str(number)[-1]
if number < 0 and int(last_d) != 0:
    print(
        f"Last digit of {number} is -{last_d} and is less than 6 and not 0")
else:
    if int(last_d) > 5:
        print(f"Last digit of {number} is {last_d} and is greater than 5")
    if int(last_d) == 0:
        print(f"Last digit of {number} is {last_d} and is 0")
