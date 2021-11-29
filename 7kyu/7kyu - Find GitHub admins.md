## Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins - 7kyu

**Instructions**

- Given the following input:

```
list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no' }
  ]
```

- Write a function that when executed as findAdmin(list1, 'JavaScript') returns only the JavaScript developers who are GitHub admins.

```
[
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' }
]
```

- Preserve the original order.

- If there are no GitHub admin developers in a given language then return an empty array [].

- The input array will always be valid.

- The strings representing whether someone is a GitHub admin will always be formatted as 'yes' and 'no'.

- The strings representing a given language will always be formatted in the same way (e.g. 'JavaScript' will always be formatted with upper-case 'J' and 'S'.

---

#### Test cases

```python
list1 = [
    {'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22,
     'language': 'JavaScript', 'githubAdmin': 'yes'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49,
     'language': 'Ruby', 'githubAdmin': 'no'},
    {'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34,
     'language': 'JavaScript', 'githubAdmin': 'yes'},
    {'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128,
     'language': 'JavaScript', 'githubAdmin': 'no'}
]

print(find_admin(list1, 'JavaScript'))
print(find_admin(list1, 'Ruby'))
print(find_admin(list1, 'Python'))
```

#### Output 

```
[{'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes'}, {'firstName': 'Jing', 'lastName': 'X.',
'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes'}]
[]
[]
```

---

#### Solution

```python
def find_admin(lst, lang):
    return [d for d in lst if d['githubAdmin'] == 'yes' and d['language'] == lang]
```

---

[Codewars link](https://www.codewars.com/kata/582dace555a1f4d859000058)
