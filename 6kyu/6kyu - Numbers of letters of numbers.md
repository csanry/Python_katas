## Numbers of Letters of Numbers - 6kyu

**Instructions**

- If we write out the digits of `60` as English words we get `sixzero`; the number of letters in `sixzero` is seven. The number of letters in `seven` is five. The number of letters in `five` is four. The number of letters in `four` is four: we have reached a stable equilibrium.

- For integers larger than 9, write out the names of each digit in a single word (instead of the proper name of the number in English). 

- For example, write 12 as `onetwo` (instead of twelve), and 999 as `nineninenine` (instead of nine hundred and ninety-nine).

- For any integer between 0 and 999, return an array showing the path from that integer to a stable equilibrium.

```
e.g.
numbers_of_letters(60) --> ["sixzero", "seven", "five", "four"]
numbers_of_letters(1) --> ["one", "three", "five", "four"]
```

---

#### Test cases

```python
print(numbers_of_letters(1))
print(numbers_of_letters(12))
print(numbers_of_letters(37))
print(numbers_of_letters(311))
print(numbers_of_letters(999))
```

#### Output 

```
['one', 'three', 'five', 'four']
['onetwo', 'six', 'three', 'five', 'four']
['threeseven', 'onezero', 'seven', 'five', 'four']
['threeoneone', 'oneone', 'six', 'three', 'five', 'four']
['nineninenine', 'onetwo', 'six', 'three', 'five', 'four']
```

---

#### Solution

```python
def numbers_of_letters(n):
    d = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', 
         '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    res = [''.join(map(d.get, str(n)))]
    while res[-1] != 'four': 
        res.append(''.join(map(d.get, str(len(res[-1])))))    
    return res
```

---

[Codewars link](https://www.codewars.com/kata/599febdc3f64cd21d8000117)
