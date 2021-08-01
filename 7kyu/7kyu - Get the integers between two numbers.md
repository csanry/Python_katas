## Get the integers between two numbers - 7kyu

**Instructions**

- Build a function that can get all the integers between two given numbers.

---

#### Test cases

```python
print(function(6, 8))
print(function(2, 9))
```

#### Output 

```
[7]
[3, 4, 5, 6, 7, 8]
```

---

#### Solution

```python
def function(start_num, end_num): 
    return [*range(start_num+1, end_num)]
```

---

[Codewars link](https://www.codewars.com/kata/598057c8d95a04f33f00004e)
