## Sum of pairs - 5kyu

**Instructions**

- Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

```
sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3 
#                ^-----^   2 + 4 = 6, indices: 2, 4 
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
```

- Negative numbers and duplicate numbers can and will appear.

---

#### Test cases

```python
print(sum_pairs([1, 4, 8, 7, 3, 15], 8))
print(sum_pairs([1, -2, 3, 0, -6, 1], -6))
print(sum_pairs([20, -13, 40], -7))
print(sum_pairs([1, 2, 3, 4, 1, 0], 2))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
print(sum_pairs([4, -2, 3, 3, 4], 8))
print(sum_pairs([0, 2, 0], 0))
print(sum_pairs([5, 9, 13, -3], 10))
```

#### Output 

```
[1, 7]
[0, -6]
None
[1, 1]
[3, 7]
[4, 4]
[0, 0]
[13, -3]
```

---

#### Solution

```python
def sum_pairs(ints, s):
    sets = set()
    for n in ints: 
        if s - n in sets: 
            return [s - n, n]
        sets.add(n)
```

---

[Codewars link](https://www.codewars.com/kata/54d81488b981293527000c8f)
