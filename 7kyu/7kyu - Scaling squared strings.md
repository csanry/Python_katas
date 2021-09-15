## Scaling squared strings - 7kyu

**Instructions**

- You are given a string of n lines, each substring being n characters long. For example:

```
s = "abcd\nefgh\nijkl\nmnop"
```

- We will study the "horizontal" and the "vertical" scaling of this square of strings.

- A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').

```
Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
```

- A v-vertical scaling of a string consists of replicating v times each part of the squared string.

```
Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
```

- Write a function to perform a k-horizontal scaling and a v-vertical scaling.

- k and v will be positive integers. If strng == "" return "".

---

#### Test cases

```python
print(scale("", 5, 5))
print(scale("Kj\nSH", 1, 2))
print(scale("abcd\nefgh\nijkl\nmnop", 2, 3))
```

#### Output 
```
""
"Kj\nKj\nSH\nSH"
"aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
```

---

#### Solution

```python
def scale(strng, k, v):
    if not strng: 
        return ''
    res = []
    for part in strng.split('\n'): 
        line = ''.join(let * k for let in part)
        for _ in range(v): 
            res.append(line)
    return '\n'.join(res)
```

---

[Codewars link](https://www.codewars.com/kata/56ed20a2c4e5d69155000301/python)
