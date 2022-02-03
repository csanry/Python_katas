## The Pony Express- 7kyu

**Instructions**

- `stations` is a list of distances in miles from one station to the next along the Pony Express route.

- Implement the `riders` function, to return how many riders are necessary to get the mail from one end to the other.

- NOTE: Each rider travels as far as he can, but never more than 100 miles.
    
---

#### Test cases

```python
print(riders([18, 15]))
print(riders([43, 23, 40, 13]))
print(riders([33, 8, 16, 47, 30, 30, 46]))
print(riders([6, 24, 6, 8, 28, 8, 23, 47, 17, 29, 37, 18, 40, 49]))
```

#### Output 

```
1
2
3
4
```

---

#### Solution

```python
def riders(stations): 
    dist, ans = 0, 1

    for s in stations: 
        if dist + s > 100: 
            ans += 1
            dist = s
        else: 
            dist += s
    return ans
```

---

[Codewars link](https://www.codewars.com/kata/5b18e9e06aefb52e1d0001e9)
