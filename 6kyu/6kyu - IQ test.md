## IQ Test - 6kyu

**Instructions**

- Bob is preparing to pass IQ test. 

- The most frequent task in this test is to find out which one of the given numbers differs from the others. 

- Bob observed that one number usually differs from the others in evenness. 

- Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

- Indexes of the elements start from 1.

```
iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even
iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd
```

---

#### Test cases

```python
print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 2"))
print(iq_test('-1 -3 -5 2'))
```

#### Output 
```
3 
1
4
```

---

#### Solution

```python
def iq_test(numbers):
    even_odd = [int(i) & 1 for i in numbers.split()]
    return even_odd.index(True) + 1 if sum(even_odd) == 1 else even.index(False) + 1
```

---

[Codewars link](https://www.codewars.com/kata/552c028c030765286c00007d)
