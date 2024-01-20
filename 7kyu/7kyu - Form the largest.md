## Form the largest - 7kyu

**Instructions**

- Given a number, return the maximum number that could be formed from the digits of the number given.

- Only Natural numbers passed to the function , numbers Contain digits [0:9] inclusive.

---

#### Test cases

```python
print(max_number(213))
print(max_number(7389))
print(max_number(63792))
print(max_number(566797))
print(max_number(1000000))
```

#### Output
```
321
9873
97632
977665
1000000
```

---

#### Solution

```python
def max_number(n):
    return int(''.join(sorted(str(n))[::-1]))
```

---

[Codewars link](https://www.codewars.com/kata/5a4ea304b3bfa89a9900008e)
