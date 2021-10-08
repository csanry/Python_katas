## Is Thue Morse - 7kyu

**Instructions**

- Given a sequence of 0s and 1s, determine if it is a prefix of Thue-Morse sequence.

- The infinite Thue-Morse sequence is obtained by first taking a sequence containing a single 0 and then repeatedly concatenating the current sequence with its binary complement.

```
0
0 1
0 1 1 0
0 1 1 0 1 0 0 1
...
```

---

#### Test cases

```python
print(is_thue_morse([0, 1, 1, 0, 1]))
print(is_thue_morse([0]))
print(is_thue_morse([1]))
print(is_thue_morse([0, 1, 0, 0]))
```

#### Output 

```
True
True
False
False
```

---

#### Solution

```python
def is_thue_morse(seq):
    start = ''.join(map(str, seq))
    x = '0110'
    while len(x) < len(start):
        x += x.translate(str.maketrans('01', '10'))
    return x.startswith(start)
```

---

[Codewars link](https://www.codewars.com/kata/589a9792ea93aae1bf00001c)
