## Alphabet symmetry - 7kyu

**Instructions**

- Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. 

- In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

- Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. 

- For example:

```python
solve(["abode", "ABc", "xyzD"]) = [4, 3, 1]
```

- Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

---

#### Test cases

```python
print(solve(["abode","ABc","xyzD"]))
print(solve(["abide","ABc","xyz"]))
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]))
print(solve(["encode","abc","xyzD","ABmD"]))
```

#### Output 
```
[4, 3, 1]
[4, 3, 0]
[6, 5, 7]
[1, 3, 1, 3]
```

---

#### Solution

```python
def solve(arr):
    return [sum(idx == ord(val.lower()) - 96 for idx, val in enumerate(word, 1)) for word in arr]
```

---

[Codewars link](https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0)
