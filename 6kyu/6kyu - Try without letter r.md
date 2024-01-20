## Try without letter "r" - 6kyu

**Instructions**

- Try to call `callme()` in a try block without the letter `r`. It means you cannot write the `try` keyword in your source because that contains letter `r`.

- You cannot use the `=` symbol.

---

#### Solution

```python
exec('t\x72y: callme()\nexcept: pass')
```

---

[Codewars link](https://www.codewars.com/kata/5b01e9f73e971587e70001ab)
