## Slaphead - 7kyu

**Instructions**

- Being a bald man myself, I know the feeling of needing to keep it clean shaven.

- You will be given a string(x). Clean shaved head is shown as "-" and stray hairs are shown as "/".

- Check the head for stray hairs and get rid of them.

- You should return the original string, but with any stray hairs removed.

- Based on the number of stray hairs removed, return:

```
0 hairs --> "Clean!"
1 hair --> "Unicorn!"
2 hairs --> "Homer!"
3-5 hairs --> "Careless!"
>5 hairs --> "Hobo!"
```

---

#### Test cases

```python
print(bald("/---------"))
print(bald("/-----/-"))
print(bald("--/--/---/-/---"))
```

#### Output

```
['----------', 'Unicorn!']
['--------', 'Homer!']
['---------------', 'Careless!']
```

---

#### Solution

```python
def bald(s):
    return [ '-' * len(s), {0: 'Clean!',
                            1: 'Unicorn!',
                            2: 'Homer!',
                            3: 'Careless!',
                            4: 'Careless!',
                            5: 'Careless!'}.get(s.count('/'), 'Hobo!')]
```

---

[Codewars link](https://www.codewars.com/kata/57efab9acba9daa4d1000b30)
