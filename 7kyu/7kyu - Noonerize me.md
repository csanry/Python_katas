## Noonerize me - 7kyu

**Instructions**

- You will create a function which takes an array of two positive integers, spoonerizes them, and returns the positive difference between them as a single number or 0 if the numbers are equal.

```
[123, 456] = 423 - 156 = 267
```

- Your code must test that all array items are numbers and return `invalid array` if it finds that either item is not a number. The provided array will always contain 2 elements.

- When the inputs are valid, they will always be integers, no floats will be passed.

- However, you must take into account that the numbers will be of varying magnitude, between and within test cases.

---

#### Test cases

```python
print(noonerize([12, 34]))
print(noonerize([55, 63]))
print(noonerize([357, 579]))
print(noonerize([1000000, 9999999]))
print(noonerize([1000000, "hello"]))
print(noonerize(["pippi", 9999999]))
print(noonerize(["pippi", "hello"]))
```

#### Output

```
18
12
178
7000001
invalid array
invalid array
invalid array
```

---

#### Solution

```python
def noonerize(numbers):
    if all(isinstance(n, int) for n in numbers):
        n1, n2 = map(str, numbers)
        new_n1 = int(n2[0] + n1[1:])
        new_n2 = int(n1[0] + n2[1:])
        return abs(new_n1 - new_n2)
    return 'invalid array'
```

---

[Codewars link](https://www.codewars.com/kata/56dbed3a13c2f61ae3000bcd)
