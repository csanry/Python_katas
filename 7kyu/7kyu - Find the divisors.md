## Find the divisors! - 7kyu

**Instructions**

- Create a function that takes an integer n > 1 and returns an array with all of the integer's divisors (except for 1 and the number itself).

- Arrange the divisors from smallest to largest.

- If the number is prime return the string '(integer) is prime'.

---

#### Test cases

```python
print(divisors(15))
print(divisors(253))
print(divisors(24))
print(divisors(25))
print(divisors(13))
print(divisors(3))
print(divisors(29))
```

#### Output
```
[3, 5]
[11, 23]
[2, 3, 4, 6, 8, 12]
[5]
13 is prime
3 is prime
29 is prime
```

---

#### Solution

```python
def divisors(integer):
    return [i for i in range(2, integer // 2 + 1) if integer % i == 0] or f"{integer} is prime"
```

---

[Codewars link](https://www.codewars.com/kata/544aed4c4a30184e960010f4)
