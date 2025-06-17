#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)  # Do not modify this line

last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

output = f"Last digit of {number} is {last_digit} and is"
if last_digit > 5:
    print(f"{output} greater than 5")
elif last_digit == 0:
    print(f"{output} 0")
else:
    print(f"{output} less than 6 and not 0")
