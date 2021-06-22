# write number in expanded form - 6kyu

"""
You will be given a number and you will need to return it as a string in Expanded Form.

For example:
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
"""

def expanded_form(num):
    st = str(num)
    return ' + '.join(str(int(num) * 10 ** pwr) for pwr, num in zip(range(len(st)-1, -1, -1), st))

print(expanded_form(12))
print(expanded_form(3273))