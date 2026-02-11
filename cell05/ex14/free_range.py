#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    start = int(args[0])
    end = int(args[1])

    if start <= end:
        numbers = list(range(start, end + 1))
    else:
        numbers = list(range(start, end - 1, -1))

    print(numbers)