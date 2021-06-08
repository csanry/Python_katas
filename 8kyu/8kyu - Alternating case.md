## altERnaTIng cAsE <=> ALTerNAtiNG CaSe - 8kyu

**Instructions**

- Given a string, return the string with the letter cases swapped.

---

#### Test cases

```python
print(to_alternating_case("hello WORLD"))
print(to_alternating_case("HeLLo WoRLD"))
print(to_alternating_case("12345"))
print(to_alternating_case("1a2b3c4d5e"))
```

#### Output 

```
HELLO world
hEllO wOrld
12345
1A2B3C4D5E
```

---

#### Solution

```python
def to_alternating_case(st):
    return st.swapcase()
```

---

[Codewars link](https://www.codewars.com/kata/56efc695740d30f963000557)
