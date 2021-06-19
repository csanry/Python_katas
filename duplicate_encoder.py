# duplicate encoder, 6kyu

'''
The goal of this exercise is to convert a string to a new string where each character in the new string is:
"(" if that character appears only once in the original string
")" if that character appears more than once in the original string
Ignore capitalization when determining if a character is a duplicate.
'''

from collections import Counter

def duplicate_encoder(word):
    cnt = Counter(word.lower())
    return ''.join('(' if cnt[c] == 1 else ')' for c in word.lower())

tests = {'din': '(((', 'recede': '()()()', 'Success': ')())())', '(( @': '))(('}

for test in tests.keys():
    print(f"Function result: {duplicate_encoder(test)} -- Expected result: {tests.get(test)}")
