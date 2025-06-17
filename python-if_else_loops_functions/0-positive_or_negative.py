#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number > 0:
    print(number, "is positive")
if number == 0:
    print(number, "is zero")
if number < 0:
    print(number, "is negative")

