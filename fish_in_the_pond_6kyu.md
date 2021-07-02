## Plenty of fish in the pond - 6kyu

**Instructions**

- In this Kata you are fish in a pond that needs to survive by eating other fish. 

- You can only eat fish that are the same size or smaller than yourself. 

- You must create a function called fish that takes a shoal of fish as an input string. 

- From this you must work out how many fish you can eat and ultimately the size you will grow to.

**Rules**

1.  Your size starts at 1

2.  The shoal string will contain fish integers between 0-9

3.  0 = algae and wont help you feed.

4.  The fish integer represents the size of the fish (1-9).

5.  You can only eat fish the same size or less than yourself.

6.  You can eat the fish in any order you choose to maximize your size.

7.  You can and only eat each fish once.

8.  The bigger fish you eat, the faster you grow. A size 2 fish equals two size 1 fish, size 3 fish equals three size 1 fish, and so on.

9.  Your size increments by one each time you reach the amounts below.


---

#### Test cases

```python
print(fish('111111111111111111112222222222'))
print(fish('151128241212192113722321331'))
print(fish('111122223333'))
```

#### Output 
```
5
5
4
```

---

#### Solution

```python
def fish(shoal):
    size = 1; eaten = 0; tot = 1
    
    for fish in sorted(map(int, shoal)):
        if fish <= size:
            eaten += fish
            if eaten >= tot * 4:
                size += 1
                tot += size
    return size
```

---


[Codewars link](https://www.codewars.com/kata/5904be220881cb68be00007d)
