## Number to digit tiers - 7kyu

**Instructions**

- Create a function that takes a number and returns an array of strings containing the number cut off at each digit.

---

#### Test cases

```python
print(create_array_of_tiers(420))
print(create_array_of_tiers(2017))
print(create_array_of_tiers(2010))
print(create_array_of_tiers(4020))
print(create_array_of_tiers(80200))
```

#### Output 

```
['4', '42', '420']
['2', '20', '201', '2017']
['2', '20', '201', '2010']
['4', '40', '402', '4020']
['8', '80', '802', '8020', '80200']
```

---

#### Solution

```python
def create_array_of_tiers(n):
    return [str(n)[:i] for i in range(1, len(str(n))+1)]
```

---

[Codewars link](https://www.codewars.com/kata/586bca7fa44cfc833e00005c)
