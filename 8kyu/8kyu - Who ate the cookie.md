## Who ate the cookie? - 8kyu

**Instructions**

- Create a program that says who ate the last cookie.

- If the input is a string then `Zach` ate the cookie.

- If the input is a float or an int then `Monica` ate the cookie.

- If the input is anything else `the dog` ate the cookie.

- The way to return the statement is: `Who ate the last cookie? It was (name)!`

---

#### Test cases

```python
print(cookie("Ryan"))
print(cookie(2.3))
print(cookie(26))
print(cookie(True))
```

#### Output

```
Who ate the last cookie? It was Zach!
Who ate the last cookie? It was Monica!
Who ate the last cookie? It was Monica!
Who ate the last cookie? It was the dog!
```

---

#### Solution

```python
def cookie(x):
    return f'Who ate the last cookie? It was {"Zach" if type(x) == str else "Monica" if type(x) in (int, float) else "the dog"}!'
```

---

[Codewars link](https://www.codewars.com/kata/55a996e0e8520afab9000055)
