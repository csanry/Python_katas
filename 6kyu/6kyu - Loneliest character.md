## Loneliest character - 6kyu

**Instructions**

- Complete the function which accepts a string and return an array of characters that have the most spaces to their right and left.

- The string can have leading / trailing spaces - you should not count them.

- The strings contain only unique characters from a to z.

- The order of characters in the returned array does not matter.

---

#### Test cases

```python
print(sorted(loneliest('a')))
print(sorted(loneliest('abc d   ef  g   h i j      ')))
print(sorted(loneliest('a   b   c ')))
print(sorted(loneliest('  abc  d  z    f gk s ')))
print(sorted(loneliest('a  b  c  de  ')))
print(sorted(loneliest('abc')))
```

#### Output

```
['a']
['g']
['b']
['z']
['b', 'c']
['a', 'b', 'c']
```

---

#### Solution

```python
import re

def loneliest(st):
    subst = [re.findall(r'\s*{}\s*'.format(let), st.strip())[0] for let in st.replace(' ', '')]
    return [let.replace(' ', '') for let in subst if len(let) == max(map(len, subst))]
```

---

[Codewars link](https://www.codewars.com/kata/5f885fa9f130ea00207c7dc8)
