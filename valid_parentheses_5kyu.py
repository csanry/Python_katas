# valid parentheses - 5kyu

'''
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples:
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
'''

def valid_parentheses(string):
    count = 0
    for c in string:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

print(valid_parentheses(")(()))"))
print(valid_parentheses("(())((()())())"))
print(valid_parentheses("hi(hi)()"))