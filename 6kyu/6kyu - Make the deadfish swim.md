## Make the Deadfish swim - 6kyu

**Instructions**

- Write a simple parser that will parse and run Deadfish.

- Deadfish has 4 commands, each 1 character long:

    - `i` increments the value (initially 0).
    
    - `d` decrements the value.
    
    - `s` squares the value.
    
    - `o` outputs the value into the return array.

- Invalid characters should be ignored.

---

#### Test cases

```python
print(parse("ooo"))
print(parse("ioioio"))
print(parse("idoiido"))
print(parse("isoisoiso"))
print(parse("codewars"))
```

#### Output 

```
[0, 0, 0]
[1, 2, 3]
[0, 1]
[1, 4, 25]
[0]
```

---

#### Solution

```python
def parse(data):
    cnt, res = 0, []
    for let in data:
        if let == 'i':
            cnt += 1
        if let == 'd':
            cnt -= 1
        if let == 's':
            cnt **= 2
        if let == 'o':
            res.append(cnt)
    return res
```

---

[Codewars link](https://www.codewars.com/kata/51e0007c1f9378fa810002a9)
