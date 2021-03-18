## Multiples of 3 or 5 - 6kyu

**Instructions**

- If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

- Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

- If the number is a multiple of both 3 and 5, only count it once.

- If a number is negative, return 0.

---

#### Test cases

```python
print(solution(0))
print(solution(-3))
print(solution(10))
print(solution(37278))
print(solution(71980))
```

#### Output 
```
0
0
23
324217950
1208916098
```

---

#### Solution

```python
def solution(number):
    return sum(range(3, number, 3)) + sum(range(5, number, 5)) - sum(range(15, number, 15))
```

---

[Codewars link](https://www.codewars.com/kata/514b92a657cdc65150000006)
