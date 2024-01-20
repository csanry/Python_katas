## For UFC Fans: Conor McGregor vs George Saint Pierre - 8kyu

**Instructions**

- Return the right statement depending on the winner!

- If the winner is George Saint Pierre he will obviously say:

    - `I am not impressed by your performance.`

- If the winner is Conor McGregor he will most undoubtedly say:

    - `I'd like to take this chance to apologize.. To absolutely NOBODY!`

- Ignore the casing of strings.

---

#### Test cases

```python
print(quote('george saint pierre'))
print(quote('conor mcgregor'))
print(quote('George Saint Pierre'))
print(quote('Conor McGregor'))
```

#### Output

```
I am not impressed by your performance.
I'd like to take this chance to apologize.. To absolutely NOBODY!
I am not impressed by your performance.
I'd like to take this chance to apologize.. To absolutely NOBODY!
```

---

#### Solution

```python
def quote(fighter):
    return {'george saint pierre': 'I am not impressed by your performance.',
            'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"}.get(fighter.lower())
```

---

[Codewars link](https://www.codewars.com/kata/582dafb611d576b745000b74)
