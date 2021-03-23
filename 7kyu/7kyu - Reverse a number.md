## Reverse a Number - 7kyu

**Instructions**

- Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

- Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

```
 123 ->  321
-456 -> -654
1000 ->    1
```

---

#### Test cases

```python
print(reverse_number(123))
print(reverse_number(-123))
print(reverse_number(1000))
print(reverse_number(4321234))
print(reverse_number(5))
print(reverse_number(0))
print(reverse_number(98989898))
```

#### Output 

```
321
-321
1
4321234
5
0
89898989
```

---

#### Solution

```python
def reverse_number(n):
    return int(str(n)[::-1]) if n >= 0 else int(str(n)[:0:-1]) * -1
```

---

[Codewars link](https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5)
