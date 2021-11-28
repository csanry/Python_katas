## Even and odd! - 7kyu

**Instructions**

- Given a number N, fabricate two numbers NE and NO such as NE is formed by even digits of N and NO is formed by odd digits of N.

- If there are no even or odd digits, return 0. 

```
126453 -> NE = 264, NO = 153
3012 -> NE = 2, NO = 31
4628 -> NE = 4628, NO = 0 
```

---

#### Test cases

```python
print(even_and_odd(126453))
print(even_and_odd(3012))
print(even_and_odd(4628))
```

#### Output 

```
(264, 153)
(2, 31)
(4628, 0)
```

---

#### Solution

```python
from itertools import filterfalse

def even_and_odd(n):
    no = ''.join(filter(lambda x: int(x) & 1, str(n)))
    ne = ''.join(filterfalse(lambda x: int(x) & 1, str(n)))
    return int(ne or 0), int(no or 0)
```

---

[Codewars link](https://www.codewars.com/kata/594adadee075005308000122/train/python)
