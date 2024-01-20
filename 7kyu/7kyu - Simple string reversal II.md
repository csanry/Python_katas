## Simple string reversal II - 7kyu

**Instructions**

- In this Kata, you will be given a string and two indexes (a and b). Your task is to reverse the portion of that string between those two indices inclusive.

```
solve("codewars",1,5) = "cawedors" -- elements at index 1 to 5 inclusive are "odewa". So we reverse them.
solve("cODEWArs", 1,5) = "cAWEDOrs" -- to help visualize.
```

- Input will be lowercase and uppercase letters only.

- The first index a will always be lower that than the string length; the second index b can be greater than the string length.

---

#### Test cases

```python
print(solve("codewars", 1, 5))
print(solve("codingIsFun", 2, 100))
print(solve("FunctionalProgramming", 2, 15))
print(solve("abcefghijklmnopqrstuvwxyz", 0, 20))
print(solve("abcefghijklmnopqrstuvwxyz", 5, 20))
```

#### Output

```
cawedors
conuFsIgnid
FuargorPlanoitcnmming
vutsrqponmlkjihgfecbawxyz
abcefvutsrqponmlkjihgwxyz
```

---

#### Solution

```python
def solve(st, a, b):
    return st[:a] + st[a:b+1][::-1] + st[b+1:]
```

---

[Codewars link](https://www.codewars.com/kata/5a8d1c82373c2e099d0000ac)
