## Consecutive Strings - 6kyu

**Instructions**

- You are given an array `strarr` of strings and an integer `k`.

- Your task is to return the first longest string consisting of `k` consecutive strings taken in the array.

---

#### Test cases

```python
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
longest_consec([], 3)
longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)
```

#### Output
```
abigailtheta
oocccffuucccjjjkkkjyyyeehh
""
wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck
```

---

#### Solution

```python
def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ''
    longest = current = sum(map(len, strarr[:k]))
    idx = 0

    for i in range(len(strarr) - k):
        current += len(strarr[i+k]) - len(strarr[i])
        if current > longest:
            longest = current
            idx = i + 1
    return ''.join(strarr[idx:idx+k])
```

---

[Codewars link](https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python)
