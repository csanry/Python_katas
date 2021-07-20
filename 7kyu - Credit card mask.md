## Credit Card Mask - 7kyu

**Instructions**

- Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

- Your task is to write a function `maskify`

- Change all but the last four characters into `'#'`.

---

#### Test cases

```python
print(maskify("4556364607935616"))
print(maskify(     "64607935616"))
print(maskify(               "1"))
print(maskify(                ""))
print(maskify("Skippy"))
print(maskify("Nananananananananananananananana Batman!"))
```

#### Output 
```
############5616
#######5616
1
""
##ippy
####################################man!
```

---

#### Solution

```python
def maskify(cc):
    return cc[-4:].rjust(len(cc), '#')

# alternative
def maskify(cc):
    return '#' * (len(cc)-4) + cc[-4:]
```

---

[Codewars link](https://www.codewars.com/kata/5412509bd436bd33920011bc)
