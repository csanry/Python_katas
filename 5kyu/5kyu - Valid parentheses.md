## Valid Parentheses - 5kyu

**Instructions**

- Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.

- The function should return true if the string is valid, and false if it's invalid.

```
Examples:
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```
---

#### Test cases

```Python
valid_parentheses(")(()))")
valid_parentheses("(())((()())())")
valid_parentheses("hi(hi)()")
```

#### Output 
```
False
True
True
```

---

#### Solution

```python
def valid_parentheses(string):
    count = 0
    for c in string:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
```

---


[Codewars link](https://www.codewars.com/kata/52774a314c2333f0a7000688)
