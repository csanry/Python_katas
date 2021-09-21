## The Skiponacci Sequence - 7kyu

**Instructions**

- Your task is to generate the Fibonacci sequence to n places, with each alternating value as `"skip"`. 

- For example:

```
"1 skip 2 skip 5 skip 13 skip 34"
```

- Return the result as a string

- You can presume that n is always a positive integer between (and including) 1 and 64.

---

#### Test cases

```python
print(skiponacci(1))
print(skiponacci(5))
print(skiponacci(7))
print(skiponacci(10))
print(skiponacci(13))
```

#### Output 
```
1
1 skip 2 skip 5
1 skip 2 skip 5 skip 13
1 skip 2 skip 5 skip 13 skip 34 skip
1 skip 2 skip 5 skip 13 skip 34 skip 89 skip 233
```

---

#### Solution

```python
def skiponacci(n):
    fib1, fib2, res = 1, 1, []
    
    for i in range(n):
        res.append('skip' if i%2 else str(fib1))
        fib1, fib2 = fib2, fib1 + fib2
    return ' '.join(res)
```

---

[Codewars link](https://www.codewars.com/kata/580777ee2e14accd9f000165)
