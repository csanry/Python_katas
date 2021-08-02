## Swap vowel case - 7kyu

**Instructions**

- Given a string, return a copy of the string with the vowels' case swapped.

- For this kata, assume that vowels are in the set "aeouiAEOUI".

- Example: Given a string "C is alive!", your function should return "C Is AlIvE!"

- Your solution is only required to work for the ASCII character set.

---

#### Test cases

```python
print(swap_vowel_case(" "))
print(swap_vowel_case("C Is AlIvE!"))
print(swap_vowel_case("to"))
print(swap_vowel_case("The"))
```

#### Output 

```

C is alive!
tO
ThE
```

---

#### Solution

```python
def swap_vowel_case(st):
    return st.translate(str.maketrans('aeiouAEIOU', 'AEIOUaeiou'))
```

---

[Codewars link](https://www.codewars.com/kata/5803c0c6ab6c20a06f000026)
