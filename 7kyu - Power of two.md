## Power of two - 7kyu

**Instructions**

- Write a function that returns if a given non-negative integer is a power of two. 

---

#### Test cases

```python
print(power_of_two(0))
print(power_of_two(1))
print(power_of_two(2))
print(power_of_two(5))
print(power_of_two(6))
print(power_of_two(4096))
```

#### Output 
```
False
True
True
False
False
True
```

---

#### Solution

```python
def power_of_two(x):
    from math import pow, log2
    return pow(2, round(log2(x))) == x if x else False

    # all power of twos will have a binary of only one 1
    # return bin(x).count('1') == 1
```

---

[Codewars link](https://www.codewars.com/kata/534d0a229345375d520006a0)
