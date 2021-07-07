## Fizz Buzz - 7kyu

**Instructions**

- Return an array containing the numbers from 1 to n, where n is the input.

- n will never be less than 1.

- Replace certain values however if any of the following conditions are met:

    - If the value is a multiple of 3: use the value `"Fizz"` instead
    
    - If the value is a multiple of 5: use the value `"Buzz"` instead
    
    - If the value is a multiple of 3 & 5: use the value `"FizzBuzz"` instead

---

#### Test cases

```python
print(fizzbuzz(16))
```

#### Output 
```
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16]
```

---

#### Solution

```python
def fizzbuzz(n):
    return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]
```

---


[Codewars link](https://www.codewars.com/kata/5300901726d12b80e8000498)
