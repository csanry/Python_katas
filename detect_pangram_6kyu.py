# detect pangram - 6kyu

'''
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram.

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
'''

import string

# checks if A is subset of B
def is_pangram(st):
    return set(string.ascii_lowercase) <= set(st.lower())

pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))