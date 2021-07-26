## TIY-FizzBuzz - 7kyu

**Instructions**

- In this exercise, you will have to create a function named tiyFizzBuzz. This function will take on a string parameter and will return that string with some characters replaced, depending on the value:
    - If a letter is a upper case consonants, replace that character with "Iron".
    
    - If a letter is a lower case consonants or a non-alpha character, do nothing to that character.
    
    - If a letter is a upper case vowel, replace that character with "Iron Yard".
    
    - If a letter is a lower case vowel, replace that character with "Yard".

---

#### Test cases

```python
print(tiy_fizz_buzz("Hello WORLD!"))
print(tiy_fizz_buzz("H6H4Na ./?U")) 
```

#### Output 
```
IronYardllYard IronIron YardIronIronIron!
Iron6Iron4IronYard ./?Iron Yard
```

---

#### Solution

```python
def tiy_fizz_buzz(st):
    return ''.join(('Iron '*c.isupper() + 'Yard'*(c.lower() in 'aeiou')).strip() or c for c in st)
```

---

[Codewars link](https://www.codewars.com/kata/5889177bf148eddd150002cc/python)
