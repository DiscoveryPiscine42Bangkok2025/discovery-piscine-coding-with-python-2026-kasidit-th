#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    text = args[0]
    result = ""

    for char in text:
        if char == "z":
            result += "z"

    if result == "":
        print("none")
    else:
        print(result)
