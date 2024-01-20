## Palindrome chain length - 7kyu

**Instructions**

- Number is a palindrome if it is equal to the number with digits in reversed order.

- For example, 5, 44, 171, 4884 are palindromes, and 43, 194, 4773 are not.

- Write a function which takes a positive integer and returns the number of special steps needed to obtain a palindrome.

- The special step is: "reverse the digits, and add to the original number".

- If the resulting number is not a palindrome, repeat the procedure with the sum until the resulting number is a palindrome.

- If the input number is already a palindrome, the number of steps is 0.

- All inputs are guaranteed to have a final palindrome smaller than 2e63.

---

#### Test cases

```python
print(palindrome_chain_length(1))
print(palindrome_chain_length(88))
print(palindrome_chain_length(87))
print(palindrome_chain_length(89))
print(palindrome_chain_length(10))
```

#### Output

```
0
0
4
24
1
```

---

#### Solution

```python
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def palindrome_chain_length(n):
    step = 0
    while not is_palindrome(n):
        step += 1
        n += int(str(n)[::-1])
    return step
```

---

[Codewars link](https://www.codewars.com/kata/525f039017c7cd0e1a000a26)
