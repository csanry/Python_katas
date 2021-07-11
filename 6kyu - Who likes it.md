## Who likes it? - 6kyu

**Instructions**

- You probably know the "like" system from Facebook and other pages.

- Implement a function `likes`, which must take in input array, 
containing the names of people who like an item.

- It must return the display text as shown in the examples:

```python
likes([]) # "no one likes this"
likes(["Peter"]) # "Peter likes this"
likes(["Jacob", "Alex"]) # "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # "Alex, Jacob and 2 others like this"
```
---

#### Test cases

```Python
likes(["Alex", "Jacob", "Mark", "Max"])
likes(["Max", "John", "Mark"])
```

#### Output 
```
Alex, Jacob and 2 like this
Max, John and Mark like this
```


---

#### Solution

```python
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} like this'
    }[min(4, n)].format(*names[:3], others = n-2)
```

---


[Codewars link](https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python)
