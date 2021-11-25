## Chuck Norris VI - Shopping with Chuck - 7kyu

**Instructions**

- Chucks action pants are extra special though. Due to his immense power, and slightly odd fan base, Chuck's used action pants actually increase in value!! That man can make money from anywhere!

- Your task, is to calculate the dollar value of a pair of used action pants owned by Chuck.

```
Inputs:
Starting price: start (dollars)
Use: soil (percentage)
Age: age (years)
```

- The action pants appreciate every year depending on the level to which they are soiled (soil input):

```
Barely used: 10%
Seen a few high kicks: 25%
Blood stained: 30%
Heavily soiled: 50%
```

- You will be given the relevant string as the soil input. Return a string prefixed with $ and to 2 decimal places.

---

#### Test cases

```python
print(price(19.95, 'Barely used', 3))
print(price(27.76, 'Seen a few high kicks', 15))
print(price(13.26, 'Blood stained', 25))
print(price(44.11, 'Heavily soiled', 7))
print(price('pants', 6, 7))
```

#### Output 

```
$26.55
$788.99
$9356.80
$753.66
Chuck is bottomless!
```

---

#### Solution

```python
D = {
    "Barely used": 1.10,
    "Seen a few high kicks": 1.25,
    "Blood stained": 1.30,
    "Heavily soiled": 1.50
}

def price(start, soil, age):
    try:
        return f'${start * D[soil] ** age:.02f}'
    except (KeyError, TypeError):
        return 'Chuck is bottomless!'
```

---

[Codewars link](https://www.codewars.com/kata/5706be574f2c297a7b00060d)
