## Coding Meetup #1 - Higher-Order Functions Series - Count the number of JavaScript developers coming from Europe - 7kyu

**Instructions**

- You will be given an array of objects representing data about developers who have signed up to attend the coding meetup that you are organising for the first time.

- Your task is to return the number of JavaScript developers coming from Europe.

---

#### Test cases

```python
list1 = [
    {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
     'language': 'JavaScript'},
    {'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28,
     'language': 'JavaScript'},
    {'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML'},
    {'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30,
     'language': 'CSS'}
]

list2 = [
    {'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 19,
     'language': 'HTML'},
    {'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria', 'continent': 'Europe', 'age': 89, 'language': 'HTML'}
]

print(count_developers(list1))
print(count_developers(list2))
```

#### Output

```
1
0
```

---

#### Solution

```python
def count_developers(lst):
    return sum(d['continent'] == 'Europe' and d['language'] == 'JavaScript' for d in lst)
```

---

[Codewars link](https://www.codewars.com/kata/582746fa14b3892727000c4f)
