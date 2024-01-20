## Char Code Calculation - 7kyu

**Instructions**

- Given a string, turn each character into its ASCII character code and join them together to create a number.

- After replacing any incidence of the number '7' with '1', return the sum of the differences in the digits of the old and the new code.

```
'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
```

```
total1 = 656667
              ^
total2 = 656661
              ^
```

```
  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6
```

---

#### Test cases

```python
print(calc('abcdef'))
print(calc('ifkhchlhfd'))
print(calc('aaaaaddddr'))
print(calc('jfmgklf8hglbe'))
print(calc('jaam'))
```

#### Output

```
6
6
30
6
12
```

---

#### Solution

```python
def calc(st):
    digits = ''.join(map(lambda x: str(ord(x)), st))
    return digits.count('7') * 6
```

---

[Codewars link](https://www.codewars.com/kata/57f75cc397d62fc93d000059)
