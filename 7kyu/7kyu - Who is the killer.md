## Who is the killer? - 7kyu

**Instructions**

- Some people have been killed!

- You have managed to narrow the suspects down to just a few.

- You also know every person who those suspects have seen on the day of the murders.

- Given a dictionary with all the names of the suspects and everyone that they have seen on that day:

```python
{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
```

- And a list of the names of the dead people:

```python
['Lucas', 'Bill']
```

- Return the name of the one killer, in our case `James` because he is the only person that saw both `Lucas` and `Bill`.

---

#### Test cases

```python
print(killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']))
print(killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben'])) 
```

#### Output 

```
James
Megan
```

---

#### Solution

```python
def killer(suspect_info, dead):
    return next(sus for sus, seen in suspect_info.items() if set(dead).issubset(seen))
```

---

[Codewars link](https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d)
