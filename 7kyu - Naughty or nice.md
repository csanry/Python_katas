## Naughty or Nice? - 7kyu

**Instructions**

- Santa needs you to write two functions. Both of the functions accept a sequence of objects. 

- The first one returns a sequence containing only the names of the nice people, and the other returns a sequence containing only the names of the naughty people. 

- Return an empty sequence [] if the result from either of the functions contains no names.

- The objects in the passed will represent people. Each object contains two properties: `name` and `was_nice`.

---

#### Test cases

```python
naughty = [{'name': 'Naughtyguy', 'was_nice': False}]
nice = [{'name': 'Santa', 'was_nice': True}, {'name': 'Warrior reading this kata', 'was_nice': True}]
print(get_nice_names(naughty))
print(get_nice_names(nice))
print(get_naughty_names(naughty))
print(get_naughty_names(nice))
```

#### Output 
```
[]
['Santa', 'Warrior reading this kata']
['Naughtyguy']
[]
```

---

#### Solution

```python
def get_nice_names(people):
    return [p['name'] for p in people if p['was_nice']]

def get_naughty_names(people):
    return [p['name'] for p in people if not p['was_nice']]
```

---

[Codewars link](https://www.codewars.com/kata/52a6b34e43c2484ac10000cd)
