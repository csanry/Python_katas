## Split Strings - 6kyu

**Instructions**

- Complete the solution so that it splits the string into pairs of two characters. 

- If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

---

#### Test cases

```python
print(solution('asdfadsf'))
print(solution('asdfads'))
print(solution(''))
print(solution('x'))
```

#### Output 
```
['as', 'df', 'ad', 'sf']
['as', 'df', 'ad', 's_']
[]
["x_"]
```

---

#### Solution

```python
def solution(s):
    if len(s) % 2: 
        s += '_'
    return [s[i:i+2] for i in range(0, len(s), 2)]
```

---

[Codewars link](https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python)
