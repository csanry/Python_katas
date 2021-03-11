## Currying Functions - 7kyu

**Instructions**

- Make a function `multiply_all` which takes an array of integers as an argument. 

- This function must return another function, which takes a single integer as an argument and returns a new array.

- The returned array should consist of each of the elements from the first array multiplied by the integer.

---

#### Test cases

```python
print(multiply_all([1, 2, 3])(1))
print(multiply_all([1, 2, 3])(2))
print(multiply_all([1, 2, 3])(0))
print(multiply_all([])(10))
```

#### Output 

```
[1, 2, 3]
[2, 4, 6]
[0, 0, 0]
[]
```

---

#### Solution

```python
def multiply_all(arr): 
    def res(x): 
        return [x * i for i in arr]
    return res
```

---

[Codewars link](https://www.codewars.com/kata/586909e4c66d18dd1800009b)
