#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
result_set = set()

for value in original_array:
    if value > 5:
        result_set.add(value + 2)

print(original_array)
print(result_set)
