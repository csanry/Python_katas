## Perfect squares, perfect fun - 7kyu

**Instructions**

- Given an integer, if the length of its digits is a perfect square, return a square block of sqroot(length) * sqroot(length).

- If not, simply return "Not a perfect square!".

---

#### Test cases

```python
print(square_it(1))
print(square_it(222))
print(square_it(234562342342))
print(square_it(88989))
print(square_it(112141568))
```

#### Output

```
1
Not a perfect square!
Not a perfect square!
Not a perfect square!
112\n141\n568
```

---

#### Solution

```python
def square_it(digits):
    st = str(digits)
    root = int(len(st)**0.5)

    if root**2 == len(st):
        return '\n'.join(st[i:i+root] for i in range(0, len(st), root))
    else:
        return 'Not a perfect square!'
```

---

[Codewars link](https://www.codewars.com/kata/5705ca6a41e5be67720012c0)
