# create phone number, 6kyu

'''
Write a function that accepts an array of 10 integers (between 0 and 9)
that returns a string of those numbers in the form of a phone number.
(XXX) XXX-XXXX
'''

def create_phone_number(n):
    st = ''.join(map(str, n))
    return f"({st[:3]}) {st[3:6]}-{st[6:]}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# expected (123) 456-7890