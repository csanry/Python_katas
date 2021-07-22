## Fizz buzz - 7kyu

**Instructions**

- Return an array containing the numbers from 1 to N, where N is the parametered value.

- If the value is a multiple of 3: use the value `"Fizz"` instead.

- If the value is a multiple of 5: use the value `"Buzz"` instead.

- If the value is a multiple of 3 & 5: use the value `"FizzBuzz"` instead.

- N will never be less than 1.

---

#### Test cases

```python
print(fizzbuzz(10))
```

#### Output 
```
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
```

---

#### Solution

```python
def fizzbuzz(n: int): 
    return ['Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or i for i in range(1, n+1)]
```

---

[Codewars link](https://www.codewars.com/kata/5300901726d12b80e8000498)
