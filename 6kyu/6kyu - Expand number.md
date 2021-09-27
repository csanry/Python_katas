## Write Number in Expanded Form - 6kyu

**Instructions**

- You will be given a number and you will need to return it as a string in Expanded Form.

- All numbers will be whole numbers greater than 0

---

#### Test cases

```python
print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(3273))
print(expanded_form(70304))
```

#### Output 
```
10 + 2
40 + 2
3000 + 200 + 70 + 3
70000 + 300 + 4
```

---

#### Solution

```python
def expanded_form(num):
    st = str(num)
    return ' + '.join(str(int(num) * 10 ** pwr) for pwr, num in zip(range(len(st)-1, -1, -1), st))
```

---


[Codewars link](https://www.codewars.com/kata/5842df8ccbd22792a4000245)
