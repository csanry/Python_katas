## Initialize my name - 7kyu

**Instructions**

- Some people just have a first name; some people have first and last names and some people have first, middle and last names.

- Initialize the middle names (if there is any).

---

#### Test cases

```python
print(initialize_names('Jack Ryan'))
print(initialize_names('Lois Mary Lane'))
print(initialize_names('Dimitri'))
print(initialize_names('Alice Betty Catherine Davis'))
```

#### Output
```
Jack Ryan
Lois M. Lane
Dimitri
Alice B. C. Davis
```

---

#### Solution

```python
def initialize_names(name):
    names = name.split()
    names[1:-1] = map(lambda x: f'{x[0]}.', names[1:-1])
    return ' '.join(names)
```

---

[Codewars link](https://www.codewars.com/kata/5768a693a3205e1cc100071f)
