## Status arrays - 7kyu

**Instructions**

- The status of each element of an array of integers can be determined by its position in the array and the value of the other elements in the array.

- The status of an element E in an array of size N is determined by adding the position P, 0 <= P < N, of the element in the array to the number of array elements in the array that are less than E.

- For example, consider the array containing the integers: `6 9 3 8 2 3 1`. The status of the element 8 is 8 because its position is 3 and there are 5 elements in the array that are less than 8.

- You will return the elements of the original array from low to high status order.

- In the event there is a tie for status of two or more elements, you will output them in order of appearance in the array.

---

#### Test cases

```python
print(status([6 ,9 ,3 ,8 ,2 ,3 ,1]))
print(status([5 ,5, 5, 8, 7, -2, -2, -3, 1, 9, 8, 3, -3, 4, -4, 6]))
print(status([14, -3, 4, 6, 9, 10, -2, 4, 0]))
```

#### Output

```
[6, 3, 2, 1, 9, 3, 8]
[5, -2, -3, 5, -2, 5, 1, -3, -4, 8, 7, 3, 4, 8, 9, 6]
[-3, 4, -2, 14, 6, 9, 4, 0, 10]
```

---

#### Solution

```python
def status(nums):
    scores, cnt = [], 0
    for i in nums:
        scores.append((sum(i > n for n in nums) + cnt, cnt))
        cnt += 1
    return [k for k, _ in sorted(zip(nums, scores), key=lambda x: (x[1][0], x[1][1]))]
```

---

[Codewars link](https://www.codewars.com/kata/601c18c1d92283000ec86f2b)
