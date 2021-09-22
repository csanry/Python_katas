## String prefix and suffix - 7kyu

**Instructions**

- Given a string, return the length of the longest prefix that is also a suffix. 

- A prefix is the start of a string while the suffix is the end of a string. 

- For instance, the prefixes of the string `"abcd"` are `["a","ab","abc"]`. The suffixes are `["bcd", "cd", "d"]`. 

- You should not overlap the prefix and suffix.

```
solve("abcd") = 0, because no prefix == suffix. 
solve("abcda") = 1, because the longest prefix which == suffix is "a".
solve("abcdabc") = 3. Longest prefix which == suffix is "abc".
solve("aaaa") = 2. Longest prefix which == suffix is "aa". You should not overlap the prefix and suffix
solve("aa") = 1. You should not overlap the prefix and suffix.
solve("a") = 0. You should not overlap the prefix and suffix.
```

---

#### Test cases

```python
print(solve("abcd"))
print(solve("abcda"))
print(solve("abcdabc"))
print(solve("abcabc"))
print(solve("abcabca"))
print(solve("aaaaa"))
print(solve("aaaa"))
print(solve("aaa"))
print(solve("aa"))
print(solve("a"))
```

#### Output 
```
0
1
3
3
1
2
2
1
1
0
```

---

#### Solution

```python
def solve(st):
    for i in range(len(st)//2, 0, -1):
        if st[:i] == st[-i:]:
            return i
    return 0

    # return next((i for i in range(len(st)//2, 0, -1) if st[:i] == st[-i:]), 0)
```

---

[Codewars link](https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1)
