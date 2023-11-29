#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nb = number
if nb < 0:
    nb *= -1
last_digit = nb % 10
if number < 0:
    last_digit *= -1
str = "Last digit of"
if last_digit > 5:
    print(f"{str} {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{str} {number} is {last_digit} and is 0")
else:
    print(f"{str} {number} is {last_digit} and is less than 6 and not 0")
