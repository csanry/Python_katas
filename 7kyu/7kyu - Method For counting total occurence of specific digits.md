## Method For Counting Total Occurence Of Specific Digits - 7kyu

**Instructions**

- Write a class `List` that contains a method `count_spec_digits`.

- `count_spec_digits` accepts two arguments, a list of integers `integers_list` and a list of digits `digits_list`. 

- Output a list of tuples, each tuple having two elements, a digit to count and its corresponding total frequency in all the integers of the first list.

- This list of tuples should be ordered with the same order provided in `digits_list`.

---

#### Test cases

```python
l = List()
print(l.count_spec_digits([1, 1, 2, 3, 1, 2, 3, 4], [1, 3]))
print(l.count_spec_digits([-18, -31, 81, -19, 111, -888], [1, 8, 4]))
print(l.count_spec_digits([-77, -65, 56, -79, 6666, 222], [1, 8, 4]))
```

#### Output 

```
[(1, 3), (3, 2)]
[(1, 7), (8, 5), (4, 0)]
[(1, 0), (8, 0), (4, 0)]
```

---

#### Solution

```python
class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        lst = ''.join(str(abs(i)) for i in integers_list)
        return [(digit, lst.count(str(digit))) for digit in digits_list]
```

---

[Codewars link](https://www.codewars.com/kata/56311e4fdd811616810000ce)
