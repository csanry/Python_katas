## Life Path Number - 7kyu

**Instructions**

- A person's Life Path Number is calculated by adding each individual number in that person's date of birth, until it is reduced to a single digit number.

- Complete the function that accepts a date of birth (as a string) in the following format: `yyyy-mm-dd`.

- The function shall return a one digit integer between 1 and 9 which represents the Life Path Number of the given date of birth.

- For example, Albert Einstein's birthday is March 14, 1879 `("1879-03-14")`.

- The calculation of his Life Path Number would look like this:

```
year  :  1 + 8 + 7 + 9 = 25  -->  2 + 5 = 7
month :  0 + 3 = 3
day   :  1 + 4 = 5
result:  7 + 3 + 5 = 15  -->  1 + 5 = 6
```

---

#### Test cases

```python
print(life_path_number('1955-10-28'))
print(life_path_number('1971-06-28'))
```

#### Output

```
4
7
```

---

#### Solution

```python
def calc_number(n):
    return int(n) % 9

def life_path_number(birthdate):
    return sum(map(calc_number, birthdate.split('-'))) % 9
```

---

[Codewars link](https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0)
