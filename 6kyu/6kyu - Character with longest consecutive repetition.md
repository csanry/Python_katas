## Character with longest consecutive repetition - 6kyu

**Instructions**

- For a given string `s` find the character `c` with longest consecutive repetition and return:

```
(c, l)
```

- `l` is the length of the repetition.

- If there are two or more characters with the same `l` return the first in order of appearance.

- For an empty string return:

```
('', 0)
```


---

#### Test cases

```python
print(longest_repetition('aaaabb'))
print(longest_repetition('bbbaaabaaaa'))
print(longest_repetition('cbdeuuu900'))
print(longest_repetition('aabb'))
print(longest_repetition(''))
```

#### Output
```
('a', 4)
('a', 4)
('u', 3)
('a', 2)
('', 0)
```

---

#### Solution

```python
def longest_repetition(chars):
    max_char, max_count = '', 0
    char, count = '', 0
    for c in chars:
        if c != char:
            char, count = c, 0
        count += 1
        if count > max_count:
            max_char, max_count = char, count
    return max_char, max_count
```

```python
# groupby solution
from itertools import groupby
def longest_repetition(chars):
    return max(((char, len(list(group))) for char, group in groupby(chars)),
                 key=lambda g: g[1], default=('', 0))
```


---


[Codewars link](https://www.codewars.com/kata/586d6cefbcc21eed7a001155)
