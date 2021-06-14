## Well of Ideas (harder version) - 7kyu

**Instructions**

- Check the provided 2 dimensional array (x) for good ideas 'good' and bad ideas 'bad'.

- If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. 

- If there are no good ideas, as is often the case, return 'Fail!'.

- The sub arrays may not be the same length.

- The solution should be case insensitive (ie good, GOOD and gOOd all count as a good idea). 

- All inputs may not be strings.

---

#### Test cases

```python
print(well([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']])) 
print(well([['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']])) 
print(well([['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']]))
```

#### Output 

```
Fail!
Publish!
I smell a series!
```

---

#### Solution

```python
def well(arr):
    num_good = sum(str(st).lower() == 'good' for subarr in arr for st in subarr)
    return {0: 'Fail!',
            1: 'Publish!', 
            2: 'Publish!'}.get(num_good, 'I smell a series!')
```

---

[Codewars link](https://www.codewars.com/kata/57f22b0f1b5432ff09001cab)
