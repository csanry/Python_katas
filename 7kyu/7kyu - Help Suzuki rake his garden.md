## Help Suzuki rake his garden! - 7kyu

**Instructions**

- Given a string representing the garden such as:

```
garden = 'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock slug ant gravel gravel snail rock gravel gravel gravel gravel gravel gravel gravel slug gravel ant gravel gravel gravel gravel rock slug gravel gravel gravel gravel gravel snail gravel gravel rock gravel snail slug gravel gravel spider gravel gravel gravel gravel gravel gravel gravel gravel moss gravel gravel gravel snail gravel gravel gravel ant gravel gravel moss gravel gravel gravel gravel snail gravel gravel gravel gravel slug gravel rock gravel gravel rock gravel gravel gravel gravel snail gravel gravel rock gravel gravel gravel gravel gravel spider gravel rock gravel gravel'
```

```
- Rake out any items that are not a rock or gravel and replace them with gravel such that:
garden = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'
- Returns a string with all items except a rock or gravel replaced with gravel:
garden = 'gravel gravel rock gravel gravel gravel gravel gravel gravel gravel'
```

---

#### Test cases

```python
garden1 = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'
garden2 = 'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock slug ant gravel gravel snail rock gravel gravel gravel gravel gravel gravel gravel slug gravel ant gravel gravel gravel gravel rock slug gravel gravel gravel gravel gravel snail gravel gravel rock gravel snail slug gravel gravel spider gravel gravel gravel gravel gravel gravel gravel gravel moss gravel gravel gravel snail gravel gravel gravel ant gravel gravel moss gravel gravel gravel gravel snail gravel gravel gravel gravel slug gravel rock gravel gravel rock gravel gravel gravel gravel snail gravel gravel rock gravel gravel gravel gravel gravel spider gravel rock gravel gravel'
print(rake_garden(garden1))
print(rake_garden(garden2))
```

#### Output 
```
'gravel gravel rock gravel gravel gravel gravel gravel gravel gravel'
'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel rock gravel gravel rock gravel gravel gravel gravel gravel gravel gravel rock gravel gravel gravel gravel gravel gravel gravel rock gravel gravel'
```

---

#### Solution

```python
def rake_garden(garden):
    return ' '.join(c if c in ('gravel', 'rock') else 'gravel' for c in garden.split())
```

---

[Codewars link](https://www.codewars.com/kata/571c1e847beb0a8f8900153d)
