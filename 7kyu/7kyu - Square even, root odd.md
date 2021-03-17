## Square Even, Root Odd - 7kyu

**Instructions**

- Complete the function that takes a list of numbers `nums`, as the only argument to the function. 

- Take each number in the list and square it if it is even, or square root the number if it is odd. 

- Take this new list and return the sum, rounded to two decimal places.

- The list will never be empty and will only contain values that are greater than or equal to zero.

---

#### Test cases

```python
print(sum_square_even_root_odd([4,5,7,8,1,2,3,0]))
print(sum_square_even_root_odd([1,14,9,8,17,21]))
```

#### Output 

```
91.61
272.71
```

---

#### Solution

```python
def sum_square_even_root_odd(nums):
    return round(sum(n**0.5 if n & 1 else n**2 for n in nums), 2)
```

---

[Codewars link](https://www.codewars.com/kata/5a4b16435f08299c7000274f)
