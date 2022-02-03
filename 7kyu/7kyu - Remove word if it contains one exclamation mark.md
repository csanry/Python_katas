## Exclamation marks: Remove words from the sentence if it contains one exclamation mark - 7kyu

**Instructions**

- Remove words from the sentence if they contain exactly one exclamation mark. 

- Words are separated by a single space, without leading/trailing spaces.
    
---

#### Test cases

```python
print(remove('Hi!')
print(remove('Hi!!!'))
print(remove('!Hi'))
print(remove('!Hi!'))
print(remove('Hi! Hi!'))
print(remove('!!!Hi !!hi!!! !hi'))
print(remove('!Hi! ! !Hi!'))
```

#### Output 

```
Hi!!!
!Hi!

!!!Hi !!hi!!!
!Hi! !Hi!
```

---

#### Solution

```python
def remove(s): 
    return ' '.join(w for w in s.split() if w.count('!') != 1)
```

---

[Codewars link](https://www.codewars.com/kata/57fafb6d2b5314c839000195/)
