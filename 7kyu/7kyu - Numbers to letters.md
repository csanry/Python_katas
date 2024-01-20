## Numbers to Letters - 7kyu

**Instructions**

- Given an array of numbers (in string format), you must return a string.

- The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc.

- You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.

- All inputs will be valid.

---

#### Test cases

```python
print(switcher(['24', '12', '23', '22', '4', '26', '9', '8']))
print(switcher(['25' ,'7' ,'8' ,'4' ,'14' ,'23' ,'8' ,'25' ,'23' ,'29' ,'16' ,'16' ,'4']))
print(switcher(['4', '24']))
print(switcher(['12']))
print(switcher(['12' ,'28' ,'25' ,'21' ,'25' ,'7' ,'11' ,'22' ,'15']))
```

#### Output

```
codewars
btswmdsbd kkw
wc
o
o?bfbtpel
```

---

#### Solution

```python
from string import ascii_lowercase

def switcher(arr):
    v = ' ?!' + ascii_lowercase
    k = map(str, range(29, 0, -1))
    d = {k: v for (k,v) in zip(k, v)}

    return ''.join(map(d.get, arr))
```

---

[Codewars link](https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c)
