## Find screen size - 7kyu

**Instructions**

- Given an integer `width` and a string `ratio` written as `WIDTH:HEIGHT`, output the screen dimensions as a string written as `WIDTHxHEIGHT`.

- The calculated height should be represented as an integer. If the height is fractional, truncate it.

---

#### Test cases

```python
print(find_screen_height(1024, "4:3"))
print(find_screen_height(1280, "16:9"))
print(find_screen_height(3840, "32:9"))
```

#### Output 

```
1024x768
1280x720
3840x1080
```

---

#### Solution

```python
def find_screen_height(width, ratio):
    d, n = map(int, ratio.split(':'))
    return f'{width}x{width * n / d:.0f}'
```

---

[Codewars link](https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f)
