## Word to binary - 7kyu

**Instructions**

- Write a function that takes a string and returns an array containing binary numbers equivalent to the ASCII codes of the characters of the string. 

- The binary strings should be eight digits long.

---

#### Test cases

```python
print(word_to_bin('man'))
print(word_to_bin('AB'))
print(word_to_bin('wecking'))
print(word_to_bin('Ruby'))
print(word_to_bin('Yosemite'))
```

#### Output 

```
['01101101', '01100001', '01101110']
['01000001', '01000010']
['01110111', '01100101', '01100011', '01101011', '01101001', '01101110', '01100111']
['01010010', '01110101', '01100010', '01111001']
['01011001', '01101111', '01110011', '01100101', '01101101', '01101001', '01110100', '01100101']
```

---

#### Solution

```python
def word_to_bin(word):
    return [f'{ord(c):08b}' for c in word]
```

---

[Codewars link](https://www.codewars.com/kata/59859f435f5d18ede7000050/)
