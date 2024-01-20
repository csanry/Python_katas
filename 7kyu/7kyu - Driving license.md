## Driving license - 7kyu

**Instructions**

- Code a UK driving license number using an array of data.

- The array looks something like:

```python
data = ["John","James","Smith","01-Jan-2000","M"]
0 = Forename
1 = Middle Name (if any)
2 = Surname
3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)
4 = M-Male or F-Female
```

**Rules**

```
1–5: The first five characters of the surname (padded with 9s if less than 5 characters)
6: The decade digit from the year of birth (e.g. for 1987 it would be 8)
7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)
9–10: The date within the month of birth
11: The year digit from the year of birth (e.g. for 1987 it would be 7)
12–13: The first two initials of the first name and middle name, padded with a 9 if no middle name
14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9
15–16: Two computer check digits. We will always use "AA"
```

---

#### Test cases

```python
data1 = ["John", "James", "Smith", "01-Jan-2000", "M"]
data2 = ["Johanna", "", "Gibbs", "13-Dec-1981", "F"]
data3 = ["Andrew", "Robert", "Lee", "02-September-1981", "M"]
print(driver(data1))
print(driver(data2))
print(driver(data3))
```

#### Output
```
SMITH001010JJ9AA
GIBBS862131J99AA
LEE99809021AR9AA
```

---

#### Solution

```python
from datetime import datetime

def driver(data):
    first, middle, last, dob, gender = data
    try:
        d = datetime.strptime(dob, '%d-%b-%Y')
    except ValueError:
        d = datetime.strptime(dob, '%d-%B-%Y')

    return '{:9<5}{[2]}{:0>2}{:0>2}{[3]}{[0]}{[0]}9AA'.format(
        last[:5].upper(),
        str(d.year),
        d.month + (50 if gender == 'F' else 0),
        d.day,
        str(d.year),
        first,
        middle if middle else '9')
```

---

[Codewars link](https://www.codewars.com/kata/586a1af1c66d18ad81000134)
