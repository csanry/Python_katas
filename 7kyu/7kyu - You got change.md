## You Got Change? - 7kyu

**Instructions**

- Create a function that will take any amount of money and break it down to the smallest number of bills as possible. Only integer amounts will be input, NO floats. 

- This function should output a sequence, where each element in the array represents the amount of a certain bill type. The array will be set up in this manner:

    - array[0] ---> represents $1 bills
    
    - array[1] ---> represents $5 bills
    
    - array[2] ---> represents $10 bills
    
    - array[3] ---> represents $20 bills
    
    - array[4] ---> represents $50 bills
    
    - array[5] ---> represents $100 bills
    
---

#### Test cases

```python
print(give_change(365))
print(give_change(217))
```

#### Output 

```
(0, 1, 1, 0, 1, 3)
(2, 1, 1, 0, 0, 2)
```

---

#### Solution

```python
def give_change(amount): 
    hundreds, rem = divmod(amount, 100)
    fifties, rem = divmod(rem, 50)
    twenties, rem = divmod(rem, 20)
    tens, rem = divmod(rem, 10)
    fives, ones = divmod(rem, 5)
    return (ones, fives, tens, twenties, fifties, hundreds)
```

---

[Codewars link](https://www.codewars.com/kata/5966f6343c0702d1dc00004c)
