## Single character palindromes II - 7kyu

**Instructions**

- Check if it is possible to convert a string to a palindrome by changing one character.

```
solve ("abbx") = True, because we can convert 'x' to 'a' and get a palindrome. 
solve ("abba") = False, because we cannot get a palindrome by changing any character. 
solve ("abcba") = True. We can change the middle character. 
```

---

#### Test cases

```python
print(solve("abba"))
print(solve("abbaa"))
print(solve("abbx"))
print(solve("aa"))
print(solve("ab"))
print(solve("abcba"))
```

#### Output 

```
False
True
True
False
True
True
```

---

#### Solution

```python
def solve(s):
    mid = len(s) // 2
    a, b = s[:mid], s[mid + len(s) % 2:][::-1]
    ans = sum(one != two for one, two in zip(a, b))
    return ans < 2 if len(s) % 2 else ans == 1
```

---

[Codewars link](https://www.codewars.com/kata/5a66ea69e6be38219f000110)
