## Sum of digits - 7kyu

**Instructions**

It involves implementing a program that sums the digits of a non-negative integer. For example, the sum of 3433 digits is 13.

Digits can be a number, a string, or None. In case of None return an empty string ''.

To give you a little more excitement, the program will not only write the result of the sum, but also write all the sums used: 3 + 4 + 3 + 3 = 13.

---

#### Test cases

```python
print(sum_of_digits("64323"))
print(sum_of_digits("8"))
print(sum_of_digits(3433))
print(sum_of_digits(64323))
print(sum_of_digits(None))
```

#### Output

```
6 + 4 + 3 + 2 + 3 = 18
8 = 8
3 + 4 + 3 + 3 = 13
6 + 4 + 3 + 2 + 3 = 18

```

---

#### Solution

```python
def sum_of_digits(digits):
    return '' if not digits else f'{" + ".join(str(digits))} = {sum(map(int, str(digits)))}'
```

---

[Codewars link](https://www.codewars.com/kata/59cf805aaeb28438fe00001c)
