## Simple directions reversal - 7kyu

**Instructions**

- In this Kata, you will be given directions and your task will be to find your way back.

```
solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"]) = ['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']
solve(['Begin on Lua Pkwy', 'Right on Sixth Alley', 'Right on 1st Cr']) =  ['Begin on 1st Cr', 'Left on Sixth Alley', 'Left on Lua Pkwy']
```

---

#### Test cases

```python
print(solve(['Begin on 3rd Blvd', 'Right on First Road', 'Left on 9th Dr']))
print(solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"]))
print(solve(["Begin on Road A"]))
```

#### Output 

```
['Begin on 9th Dr', 'Right on First Road', 'Left on 3rd Blvd']
['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']
['Begin on Road A']
```

---

#### Solution

```python
def solve(arr):
    dir, loc = zip(*(s.split(' ', 1) for s in arr))
    reverse = ['Begin'] + ['Right' if s == 'Left' else 'Left' for s in dir[:0:-1]]
    return [' '.join(i) for i in zip(reverse, loc[::-1])]
```

---

[Codewars link](https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca)
