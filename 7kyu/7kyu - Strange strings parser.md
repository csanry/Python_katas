## Strange strings parser - 7kyu

**Instructions**

- Find the special character, split by that character, and return a list of parts.

---

#### Test cases

```python
print(word_splitter("12:56C:144:1000:1200"))
print(word_splitter("23;RPM;300;PSI;MODE;FORWARD"))
print(word_splitter("340000.00*-140.49902*ELEVATION*24000000*END"))
```

#### Output 

```
['12', '56C', '144', '1000', '1200']
['23', 'RPM', '300', 'PSI', 'MODE', 'FORWARD']
['340000.00', '-140.49902', 'ELEVATION', '24000000', 'END']
```

---

#### Solution

```python
import re
def word_splitter(string):
    return re.split(r'[^\w\.-]', string)
```

---

[Codewars link](https://www.codewars.com/kata/584d88622609c8bda30000cf)
