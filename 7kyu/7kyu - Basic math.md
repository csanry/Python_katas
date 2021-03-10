## Basic Math (Add or Subtract) - 7kyu

**Instructions**

- Do addition and subtraction on a given string.

- The return value must be also a string.

---

#### Test cases

```python
print(calculate('1plus2plus3plus4'))
print(calculate('1minus2minus3minus4'))
print(calculate('1plus2plus3minus4'))
```

#### Output 

```
10
-8
2
```

---

#### Solution

```python
def calculate(s):
    return str(sum(int(n) for n in s.replace("minus", "plus-").split("plus")))
    
    # eval not recommended as best practice
    # return f"{eval(s.replace('plus', '+').replace('minus', '-'))}"
```

---

[Codewars link](https://www.codewars.com/kata/5809b62808ad92e31b000031)
