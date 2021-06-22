# narcissistic numbers - 6kyu

"""
The Challenge:
Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.
Error checking for text strings or other invalid inputs is not required.
Only valid positive non-zero integers will be passed into the function.

A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
In this Kata, we will restrict ourselves to decimal (base 10).
"""

def narcissistic(value):
    pwr = len(str(value))
    return sum(map(lambda x: int(x) ** pwr, list(str(value)))) == value

print(narcissistic(153))
print(narcissistic(1652))