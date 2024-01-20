## Sum of integers in string - 7kyu

**Instructions**

- Implement a function that calculates the sum of the integers inside a string.

- For example, in the string `"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"`, the sum of the integers is `3635`.

- Note: only positive integers will be tested.

---

#### Test cases

```python
print(sum_of_integers_in_string("Our company made approximately 1 million in gross revenue last quarter."))
print(sum_of_integers_in_string("The Great Depression lasted from 1929 to 1939."))
print(sum_of_integers_in_string("Dogs are our best friends."))
print(sum_of_integers_in_string("C4t5 are 4m4z1ng."))
print(sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
```

#### Output
```
1
3868
0
18
3635
```

---

#### Solution

```python
def sum_of_integers_in_string(s):
    import re
    return sum(map(int, re.findall(r'\d+', s)))
```

---

[Codewars link](https://www.codewars.com/kata/598f76a44f613e0e0b000026)
