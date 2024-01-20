## Coding Meetup - Will all continents be represented? - 6kyu

**Instructions**

- You will be given a sequence of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

- Return `True` if all of the following continents / geographic zones will be represented by at least one developer: `'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'`.

- Return `False` otherwise.

---

#### Test cases

```python
list1 = [
    {'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript'},
    {'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C'},
    {'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby'},
    {'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby'},
    {'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP'}
]

list2 = [{'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript'}]

print(all_continents(list1))
print(all_continents(list2))
```

#### Output

```
True
False
```

---

#### Solution

```python
def all_continents(lst):
    return set(['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']) == set(d['continent'] for d in lst)
```

---

[Codewars link](https://www.codewars.com/kata/58291fea7ff3f640980000f9)
