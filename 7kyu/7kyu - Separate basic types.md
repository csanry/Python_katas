## Separate basic types - 7kyu

**Instructions**

- Given a sequence of different type of values (number, string, boolean), return an object with a separate properties for each of types presented in input. 

- Each property should contain an array of corresponding values.

- Keep the original order of values in the array.

- If type is not presented in input, no corresponding property is expected.

For this input:

```
['a', 1, 2, False, 'b']
```

Expected output is:

```
{
  int: [1, 2],
  str: ['a', 'b'],
  bool: [False]
}
```

---

#### Test cases

```python
print(separate_types(['a', 1, 2, False, 'b']))
print(separate_types(['a', 1, 2]))
```

#### Output 

```
defaultdict(<class 'list'>, {<class 'str'>: ['a', 'b'], <class 'int'>: [1, 2], <class 'bool'>: [False]})
defaultdict(<class 'list'>, {<class 'str'>: ['a'], <class 'int'>: [1, 2]})
```

---

#### Solution

```python
from collections import defaultdict

def separate_types(seq): 
    res = defaultdict(list)
    for e in seq:     
        res[type(e)].append(e)
    return res
```

---

[Codewars link](https://www.codewars.com/kata/60113ded99cef9000e309be3)
