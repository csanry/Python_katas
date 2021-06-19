# replace with alphabet position - 6kyu

'''
Given a string, replace every letter with its position in the alphabet.
Ignore anything in the text that isn't a letter.
eg. alphabet_position("The") should return "20 8 5"
'''

def alphabet_position(text):
    return ' '.join(str(ord(let) - 96) for let in text.lower() if let.isalpha())

print(alphabet_position("The sunset sets at twelve o'clock."))
