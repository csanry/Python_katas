## Olympic rings - 7kyu

**Instructions**

- Given a string of random letters, you need to examine each. 

- Some letters naturally have 'rings' in them. 'O' is an obvious example, but 'b', 'p', 'e', 'A', etc are all just as applicable. 'B' even has two!! Please note for this kata you can count lower case 'g' as only one ring.

- Count the 'rings' in each letter and divide the total number by 2 and round the answer down. 

- Once you have your final score:

    - If score is 1 or less, return 'Not even a medal!'; if score is 2, return 'Bronze!'; if score is 3, return 'Silver!'; if score is more than 3, return 'Gold!'.

- Dots over i's and any other letters don't count as rings.

---

#### Test cases

```python
print(olympic_ring('wHjMudLwtoPGocnJ'))
print(olympic_ring('eCEHWEPwwnvzMicyaRjk'))
print(olympic_ring('JKniLfLW'))
print(olympic_ring('EWlZlDFsEIBufsalqof'))
print(olympic_ring('IMBAWejlGRTDWetPS'))
```

#### Output 

```
Bronze!
Bronze!
Not even a medal!
Silver!
Gold!
```

---

#### Solution

```python
def olympic_ring(string):
    one_ring = 'ADOPQRabdegopq'
    num_rings = sum(map(lambda x: 1 if x in one_ring 
                        else 2 if x == 'B' else 0, string)) // 2
    return {num_rings <= 1: 'Not even a medal!', 
            num_rings == 2: 'Bronze!', 
            num_rings == 3: 'Silver!', 
            num_rings > 3: 'Gold!'}.get(True, None)
```

---

[Codewars link](https://www.codewars.com/kata/57d06663eca260fe630001cc/)
