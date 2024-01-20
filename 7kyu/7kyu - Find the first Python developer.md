## Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer - 7kyu

**Instructions**

- Given a list of data about developers who have signed up to attend the next coding meetup, return either:

- The first Python developer who has signed up, formatted as `<first_name>, <country>`

- The string `There will be no Python developers` if no Python developer has signed up.

- The list is ordered according to who signed up first.

---

#### Test cases

```python
list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]

list2 = [
  { "first_name": "Kseniya", "last_name": "T.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript" },
  { "first_name": "Amar", "last_name": "V.", "country": "Bosnia and Herzegovina", "continent": "Europe", "age": 32, "language": "Ruby" }
]

print(get_first_python(list1))
print(get_first_python(list2))
```

#### Output

```
Victoria, Puerto Rico
There will be no Python developers
```

---

#### Solution

```python
def get_first_python(users):
    for d in users:
        if d['language'] == 'Python':
            return f'{d["first_name"]}, {d["country"]}'
    return 'There will be no Python developers'
```

---

[Codewars link](https://www.codewars.com/kata/5827bc50f524dd029d0005f2)
