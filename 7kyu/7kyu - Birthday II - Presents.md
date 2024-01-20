## Birthday II - Presents - 7kyu

**Instructions**

- Your colleagues have been good enough to buy you a birthday gift.

- Even though it is your birthday and not theirs, they have decided to play pass the parcel with it so that everyone has an even chance of winning.

- There are multiple presents, and you will receive one, but not all are nice... one even explodes and covers you in soil... strange office.

- To make up for this one present is a dog! Happy days! (do not buy dogs as presents, and if you do, never wrap them).

- Depending on the number of passes in the game (y), and the present you unwrap (x), return as follows:

    - x = goodpresent > return x with num of passes added to each charCode (turn to charCode, add y to each, turn back).

    - x = crap or x = empty > return string sorted alphabetically.

    - x = bang > return string turned to char codes, each code reduced by number of passes and summed to a single figure.

    - x = badpresent > return `Take this back!`.

    - x = dog, return `pass out from excitement y times` (where y is the value given for y).

---

#### Test cases

```python
print(present("badpresent", 3))
print(present("goodpresent", 9))
print(present("crap", 10))
print(present("bang", 27))
print(present("dog", 23))
```

#### Output

```
Take this back!
pxxmy{n|nw}
acpr
300
pass out from excitement 23 times
```

---

#### Solution

```python
def present(x,y):
    if x == 'goodpresent':
        return ''.join(chr(ord(c) + y) for c in x)
    elif x in ('crap', 'empty'):
        return ''.join(sorted(x))
    elif x == 'bang':
        return str(408 - 4 * y)
    elif x == 'dog':
        return f'pass out from excitement {y} times'
    elif x == 'badpresent':
        return 'Take this back!'
    else:
        return ''
```

---

[Codewars link](https://www.codewars.com/kata/5805f0663f1f9c49be00011f/)
