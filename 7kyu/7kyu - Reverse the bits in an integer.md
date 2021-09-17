## Reverse the bits in an integer - 7kyu

**Instructions**

- Write a function that reverses the bits in an integer.

- For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

- You can assume that the number is not negative.

---

#### Test cases

```python
print(reverse_bits(417))
print(reverse_bits(267))
print(reverse_bits(0))
print(reverse_bits(2017))
print(reverse_bits(1024))
print(reverse_bits(1023))
```

#### Output 
```
267
417
0
1087
1
1023
```

---

#### Solution

```python
def reverse_bits(n):
    return int(bin(n)[:1:-1], 2)
```

---

[Codewars link](https://www.codewars.com/kata/5959ec605595565f5c00002b)
