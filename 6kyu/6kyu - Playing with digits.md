## Playing with digits - 6kyu

**Instructions**

- Some numbers have funny properties. For example:

```
89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
```

- Given a positive integer `n` written as abcd... (a, b, c, d... being digits) and a positive integer `p`.

- Find a positive integer `k`, if it exists, such as the sum of the digits of `n` taken to the successive powers of `p` is equal to `k * n`.

- If `k` exists, return `k`, if not return `-1`.

- `n` and `p` will always be given as strictly positive integers.

---

#### Test cases

```python
print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
```

#### Output

```
1
-1
51
```

---

#### Solution

```python
def dig_pow(n, p):
    k, fail = divmod(sum(int(v) ** i for i, v in enumerate(str(n), p)), n)
    return -1 if fail else k
```

---

[Codewars link](https://www.codewars.com/kata/5552101f47fc5178b1000050)
