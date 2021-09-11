## Kaprekar Split - 7kyu

**Instructions**

- A number is a Kaprekar number if its square can be split up into two parts which sum up to the original number.

- Create a function that, if the input is a Kaprekar number, outputs the index that splits the square into the two parts that sum to the original number. 

- For non-Kaprekar numbers, the output should be -1.

---

#### Test cases

```python
print(kaprekar_split(1))
print(kaprekar_split(9))
print(kaprekar_split(45))
print(kaprekar_split(2223))
print(kaprekar_split(5050))
print(kaprekar_split(5051))
```

#### Output 
```
0
1
2
3
4
-1
```

---

#### Solution

```python
def kaprekar_split(n):
    sq = str(n ** 2)
    for i in range(len(n)):
        if int(sq[:i] or 0) + int(sq[i:] or 0) == n:
            return i
    return -1
```

---

[Codewars link](https://www.codewars.com/kata/5b6ee22ac5cc71833f0010d7)
