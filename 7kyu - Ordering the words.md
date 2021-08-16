## Ordering the words! - 7kyu

**Instructions**

- Given a string, write a method that orders every letter in the string in ascending order.

- Validate that the given string is not empty or null. If so, return `Invalid String!`



---

#### Test cases

```python
print(order_word("Hello, World!"))
print(order_word("bobby"))
print(order_word(""))
```

#### Output 
```
 !,HWdellloor
bbboy
Invalid String!
```

---

#### Solution

```python
def order_word(s):
    return ''.join(sorted(s)) if s else 'Invalid String!'
```

---

[Codewars link](https://www.codewars.com/kata/55d7e5aa7b619a86ed000070)
