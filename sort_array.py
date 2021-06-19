# sort the odd, 7kyu

"""
Task:
Given an array of numbers, sort the odd numbers in ascending order while leaving the even numbers
at their original positions.

Input: array of integers
"""

def sort_array(input_arr):
    odds = sorted(x for x in input_arr if x & 1)
    return [odds.pop(0) if n & 1 else n for n in input_arr]

print(sort_array([5, 3, 2, 8, 1, 4]))