## A rule of divisibility by 7 - 7kyu

**Instructions**

- A number m of the form 10x + y is divisible by 7 if and only if x − 2y is divisible by 7. 

- Continue to do this until a number known to be divisible by 7 is obtained. 

- The original number is divisible by 7 if and only if the last number obtained using this procedure is divisible by 7.

- Your task is to return to the function seven(m) (m integer >= 0) a tuple of numbers. 

- The first being the last number m with at most 2 digits obtained by your function (this last m will be divisible or not by 7).

- Stop the process when m has at most 2 digits because you are supposed to know if a number of at most 2 digits is divisible by 7 or not.

- The second one being the number of steps to get the result.

---

#### Test cases

```python
print(seven (1603))
print(seven (371))
print(seven (483))
print(seven(1021))
```

#### Output 
```
(7, 2)
(35, 1)
(42, 1)
(10, 2)
```

---

#### Solution

```python
def seven(m): 
    res, counter = m, 0 
    while res > 99:
        q, r = divmod(res, 10)
        res = q - (2 * r)
        counter += 1
    return res, counter
```

---

[Codewars link](https://www.codewars.com/kata/55e6f5e58f7817808e00002e)
