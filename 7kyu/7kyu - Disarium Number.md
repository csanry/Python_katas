## Disarium Number - 7kyu

**Instructions**

- A Disarium number is a number where the sum of its digits powered with their respective positions is equal to the number itself.

- Number passed is always positive. 

- Return `"Disarium !!"` if the number is Disarium else `"Not !!"`

---

#### Test cases

```python
print(disarium_number(89))
print(disarium_number(518))
print(disarium_number(1024))
```

#### Output 
```
Disarium !!
Disarium !!
Not !!
```

---

#### Solution

```python
def disarium_number(n):
    return ['Not !!', 'Disarium !!'][n == sum(int(val) ** idx for idx, val in enumerate(str(n), 1))]
```

---

[Codewars link](https://www.codewars.com/kata/5a53a17bfd56cb9c14000003)
