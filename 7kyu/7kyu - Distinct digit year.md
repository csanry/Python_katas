## Distinct digit year - 7kyu

**Instructions**

- Given a year number, output the minimum year number which is strictly larger than the given one and has only distinct digits.

- 1000 <= year <= 9000

---

#### Test cases

```python
print(distinct_digit_year(5855))
print(distinct_digit_year(5154))
print(distinct_digit_year(1060))
print(distinct_digit_year(1823))
```

#### Output
```
5860
5160
1062
1824
```

---

#### Solution

```python
def distinct_digit_year(year):
    year += 1
    while len(set(str(year))) != 4:
        year += 1
    return year
```

---

[Codewars link](https://www.codewars.com/kata/58aa68605aab54a26c0001a6)
