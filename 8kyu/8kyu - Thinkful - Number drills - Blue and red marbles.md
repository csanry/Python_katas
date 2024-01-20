## Thinkful - Number Drills: Blue and red marbles - 8kyu

**Instructions**

- Given:

    - The number of blue marbles you put in the bag to start.

    - The number of red marbles you put in the bag to start.

    - The number of blue marbles pulled out so far (always lower than the starting number of blue marbles).

    - The number of red marbles pulled out so far (always lower than the starting number of red marbles).

- Return the probability of drawing a blue marble, expressed as a float.

- For example, `guess_blue(5, 5, 2, 3)` should return `0.6`.

---

#### Test cases

```python
print(guess_blue(5, 5, 2, 3))
print(guess_blue(5, 7, 4, 3))
print(guess_blue(12, 18, 4, 6))
```

#### Output

```
0.6
0.2
0.4
```

---

#### Solution

```python
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    bl = blue_start - blue_pulled
    rl = red_start - red_pulled
    return bl / (bl + rl)
```

---

[Codewars link](https://www.codewars.com/kata/5862f663b4e9d6f12b00003b)
