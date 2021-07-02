## Roman Numerals Decoder - 6kyu

**Instructions**

- Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 

- You don't need to validate the form of the Roman numeral.

- Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. 

- So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). 

```
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
```

---

#### Test cases

```python
print(solution('XXI'))
print(solution('I'))
print(solution('IV'))
print(solution('MMVIII'))
print(solution('MDCLXVI'))
```

#### Output 
```
21
1
4
2008
1666
```

---

#### Solution

```python
def solution(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
    sum = 0; last = 0
    for c in roman: 
        sum += values[c]
        if values[c] > last: 
            sum -= 2 * last
        last = values[c]
    return sum
```

---


[Codewars link](https://www.codewars.com/kata/51b6249c4612257ac0000005)
