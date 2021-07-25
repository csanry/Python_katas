## Alphabet war - 7kyu

**Instructions**

- There is a war and nobody knows - the alphabet war!

- There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

- Write a function that accepts `fight` string consists of only small letters and return who wins the fight. When the left side wins return `Left side wins!`, when the right side wins return `Right side wins!`, in other case return `Let's fight again!`.

The left side letters and their power:
```
 w - 4
 p - 3
 b - 2
 s - 1
```

The right side letters and their power: 
```
 m - 4
 q - 3
 d - 2
 z - 1
```

---

#### Test cases

```python
print(alphabet_war("z"))       
print(alphabet_war("zdqmwpbs")) 
print(alphabet_war("zzzzs"))    
print(alphabet_war("wwwwwwz"))  
```

#### Output 
```
Right side wins!
Let's fight again!
Right side wins!
Left side wins!
```

---

#### Solution

```python
def alphabet_war(fight): 
    d = {'w': 4, 'p': 3, 'b': 2, 's': 1,
         'm': -4, 'q': -3, 'd': -2, 'z': -1}
    res = sum(d[c] for c in fight if c in d.keys())
    return {res == 0: "Let's fight again!", 
            res > 0: "Left side wins!", 
            res < 0: "Right side wins!"}[True]
```

---

[Codewars link](https://www.codewars.com/kata/59377c53e66267c8f6000027)
