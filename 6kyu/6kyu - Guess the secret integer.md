## Guess the secret integer - 6kyu

**Instructions**

- Return the secret integer in a range based on the response from the `guess_bot`.

- You are given a `low` and `high` range (inclusive) and an instance of `guess_bot`.

- You are only to interact with `guess_bot` by its method: `guess_number(num)` which returns a string.

- `guess_bot` is a bit of an asshole and only returns the following strings when you call `guess_number(number)`:

    - `'Smaller'`: Your guess is too big

    - `'Larger'`: Your guess is too small

    - `'Correct'`: Your guess is correct

    - `'You failed, you bring great shame to your family name'`: You ran out of tries

    - `'What are you, deaf?'`: Returned if you continously call guess_number after you already guessed the correct number

    - You only have log2(N) calls to guess_number before the bot starts calling you a failure. N is the number of possible integers in the [low, high] range.

- 1 <= N <= 10^14

---

#### Solution

```python
def find_secret_number(low, high, guess_bot):
    start = low
    end = high

    while start <= end:
        mid = (start + end) // 2
        ans = guess_bot.guess_number(mid)
        if ans == 'Correct':
            return mid
        elif ans == 'Larger':
            start = mid + 1
        else:
            end = mid - 1
```

---

[Codewars link](https://www.codewars.com/kata/5749b2fc8bf8b6fbd3001ff3)
