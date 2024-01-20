## The animals went in two by two - 7kyu

**Instructions**

- A great flood has hit the land, and we need to get the animals to the ark in pairs.

- You will be given a list of animals, which you need to check to see which animals there are at least two of.

- Return a dictionary containing the name of the animal along with the fact that there are 2 of them to bring onto the ark.

- If the list of animals is empty, return False as there are no animals to bring onto the ark.

- If there are no pairs of animals, return an empty dictionary.

---

#### Test cases

```python
print(two_by_two([]))
print(two_by_two(['goat']))
print(two_by_two(["dog", "cat", "dog", "cat", "beaver", "cat"]))
print(two_by_two(["goat", "goat", "rabbit", "rabbit", "rabbit", "duck", "horse", "horse", "swan"]))
```

#### Output
```
False
{}
{'dog': 2, 'cat': 2}
{'horse': 2, 'goat': 2, 'rabbit': 2}
```

---

#### Solution

```python
def two_by_two(animals):
    return {a: 2 for a in set(animals) if animals.count(a) > 1} if animals else False
```

---

[Codewars link](https://www.codewars.com/kata/578de3801499359921000130)
