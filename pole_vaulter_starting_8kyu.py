# pole vaulter starting point - 8kyu

'''
You are given the following two guidelines to begin with:
1. A vaulter with a height of 1.52 meters should start at 9.45 meters on the runway.
2. A vaulter with a height of 1.83 meters should start at 10.67 meters on the runway.

You will receive a vaulter's height in meters.
The vaulter's height will always lie in a range between a minimum of 1.22 meters and a maximum of 2.13 meters.
Return the best starting mark in meters, rounded to two decimal places.
Assume there is a linear relationship between height of the vaulter and the start point.
'''

def starting_mark(height):
    m = (10.67 - 9.45) / (1.83 - 1.52)
    c = 10.67 - m * 1.83
    return round(m * height + c, 2)

print(starting_mark(1.75))
print(starting_mark(1.83))
print(starting_mark(2.01))