## Coding Meetup #2 - Higher-Order Functions Series - Greet developers - 7kyu

**Instructions**

- You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

- Return an array where each object will have a new property `greeting` with the following string value:

```
Hi < firstName here >, what do you like the most about < language here >?
```

---

#### Test cases

```python
list1 = [
    {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
     'language': 'Java'},
    {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
     'language': 'Python'},
    {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
     'language': 'Ruby'}]

print(greet_developers(list1))
```

#### Output 

```
[{'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
 'language': 'Java',
 'greeting': 'Hi Sofia, what do you like the most about Java?'
 },
{'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
 'language': 'Python',
 'greeting': 'Hi Lukas, what do you like the most about Python?'
 },
{'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
 'language': 'Ruby',
 'greeting': 'Hi Madison, what do you like the most about Ruby?'
 }]
```

---

#### Solution

```python
def greet_developers(lst): 
    for d in lst: 
        d['greeting'] = f'Hi {d["firstName"]}, what do you like the most about {d["language"]}?'
    return lst
```

---

[Codewars link](https://www.codewars.com/kata/58279e13c983ca4a2a00002a)
