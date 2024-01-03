#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lasdig = repr(number)[-1]
if number < 0:
    print(f"Last digit of {number} is {lasdig} and is less than 6 and not 0")
elif int(lasdig) > 5:
    print(f"Last digit of {number} is {lasdig} and is greater than 5")
elif int(repr(number)[-1]) == 0:
    print(f"Last digit of {number} is {lasdig} and is 0")
else:
    print(f"Last digit of {number} is {lasdig} and is less than 6 and not 0")
