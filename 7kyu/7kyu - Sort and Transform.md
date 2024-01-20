## Sort and Transform - 7kyu

**Instructions**

- Given an array of numbers, return a string made up of four parts:

- A four character 'word', made up of the characters derived from the first two and last two numbers in the array, converted to ASCII.

- The same as above, post sorting the array by ascending order.

- The same as above, post sorting the array into descending order.

- The same as above, post converting the array into ASCII characters and sorting alphabetically.

- The four parts should form a single string, each part separated by a hyphen (-).

- Example format of solution: "asdf-tyui-ujng-wedg"

**Examples**

```python
[111, 112, 113, 114, 115, 113, 114, 110]  -->  "oprn-nors-sron-nors"
[66, 101, 55, 111, 113]                   -->  "Beoq-7Boq-qoB7-7Boq"
[99, 98, 97, 96, 81, 82, 82]              -->  "cbRR-QRbc-cbRQ-QRbc"
```

---

#### Test cases

```python
print(sort_transform([111, 112, 113, 114, 115, 113, 114, 110]))
print(sort_transform([51, 62, 73, 84, 95, 100, 99, 126]))
print(sort_transform([66, 101, 55, 111, 113]))
print(sort_transform([78, 117, 110, 99, 104, 117, 107, 115, 120, 121, 125]))
print(sort_transform([101, 48, 75, 105, 99, 107, 121, 122, 124]))
print(sort_transform([80, 117, 115, 104, 65, 85, 112, 115, 66, 76, 62]))
print(sort_transform([78, 93, 92, 98, 108, 119, 116, 100, 85, 80]))
print(sort_transform([111, 121, 122, 124, 125, 126, 117, 118, 119, 121, 122, 73]))
print(sort_transform([82, 98, 72, 71, 71, 72, 62, 67, 68, 115, 117, 112, 122, 121, 93]))
print(sort_transform([99, 98, 97, 96, 81, 82, 82]))
print(sort_transform([66, 99, 88, 122, 123, 110]))
print(sort_transform([66, 87, 98, 59, 57, 50, 51, 52]))
```

#### Output
```
oprn-nors-sron-nors
3>c~-3>d~-~d>3-3>d~
Beoq-7Boq-qoB7-7Boq
Nuy}-Ncy}-}ycN-Ncy}
e0z|-0Kz|-|zK0-0Kz|
PuL>->Asu-usA>->Asu
N]UP-NPtw-wtPN-NPtw
oyzI-Io}~-~}oI-Io}~
Rby]->Cyz-zyC>->Cyz
cbRR-QRbc-cbRQ-QRbc
Bc{n-BXz{-{zXB-BXz{
BW34-23Wb-bW32-23Wb
```

---

#### Solution

```python
def as_string(arr):
    return ''.join(map(chr, arr[:2] + arr[-2:]))

def sort_transform(arr):
    return '-'.join([
            as_string(arr),
            as_string(sorted(arr)),
            as_string(sorted(arr, reverse=True)),
            as_string(sorted(arr))
            ])
```

---

[Codewars link](https://www.codewars.com/kata/57cc847e58a06b1492000264)
