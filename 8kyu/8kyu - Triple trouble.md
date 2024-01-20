## Triple Trouble - 8kyu

**Instructions**

- Create a function that will return a string that combines all of the letters of the three input strings in groups.

```
E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
```

---

#### Test cases

```python
print(triple_trouble("aaa" ,"bbb" ,"ccc"))
print(triple_trouble("aaaaaa" ,"bbbbbb" ,"cccccc"))
print(triple_trouble("burn", "reds", "roll"))
print(triple_trouble("Bm", "aa", "tn"))
```

#### Output

```
abcabcabc
abcabcabcabcabcabc
brrueordlnsl
Batman
```

---

#### Solution

```python
def triple_trouble(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))
```

---

[Codewars link](https://www.codewars.com/kata/5704aea738428f4d30000914)
