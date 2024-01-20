## Fizz/Buzz - 7kyu

**Instructions**

- Write a function that takes an integer and returns an array `[A, B, C]`.

- `A` is the number of multiples of 3 (but not 5) below the given integer

- `B` is the number of multiples of 5 (but not 3) below the given integer

- `C` is the number of multiples of 3 and 5 below the given integer.

- For example, `solution(20)` should return `[5, 2, 1]`

---

#### Test cases

```python
print(solution(20))
print(solution(2))
print(solution(14))
print(solution(30))
print(solution(141))
```

#### Output
```
[5, 2, 1]
[0, 0, 0]
[4, 2, 0]
[8, 4, 1]
[37, 19, 9]
```

---

#### Solution

```python
def solution(number):
    number -= 1
    C = number // 15
    A = number // 3 - C
    B = number // 5 - C
    return [A, B, C]
```

---


[Codewars link](https://www.codewars.com/kata/51dda84f91f5b5608b0004cc)
