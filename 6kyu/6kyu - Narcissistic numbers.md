## Narcissistic numbers - 6kyu

**Instructions**

- Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.

- Error checking for text strings or other invalid inputs is not required.

- Only valid positive non-zero integers will be passed into the function.

- A narcissistic number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.

- In this Kata, we will restrict ourselves to decimal (base 10).

---

#### Test cases

```python
print(narcissistic(9))
print(narcissistic(153))
print(narcissistic(1652))
```

#### Output

```
True
True
False
```

---

#### Solution

```python
def narcissistic(value):
    pwr = len(str(value))
    return sum(int(x) ** pwr for x in str(value)) == value
```

---

[Codewars link](https://www.codewars.com/kata/5287e858c6b5a9678200083c)
