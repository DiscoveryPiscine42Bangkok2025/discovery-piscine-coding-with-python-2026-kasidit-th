#!/usr/bin/env python3

number = input("Give me a number: ")

if "." in number:
    if float(number).is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
else:
    print("This number is an integer.")