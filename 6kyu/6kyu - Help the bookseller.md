## Help the bookseller ! - 6kyu

**Instructions**

- A bookseller has lots of books classified in 26 categories labeled A, B, ... Z.

- Each book has a code c of 3, 4, 5 or more characters.

- The 1st character of a code is a capital letter which defines the book category.

- In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

- For example an extract of a stocklist could be:

```
L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}
```
- Given a stocklist `L` and a list of categories `M`

- Find all the books in `L` with codes belonging to each category in `M` and sum their quantity

```
(A : 20) - (B : 114) - (C : 50) - (W : 0)
```

---

#### Test cases

```python
b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print((stock_list(b, c))
```

#### Output
```
(A : 200) - (B : 1140)
```

---

#### Solution

```python
def stock_list(bookstore, categories):
    from collections import defaultdict
    if not bookstore or not categories:
        return ''
    cnt = defaultdict(int)

    for book in bookstore:
        category, quantity = book.split()[0][0], int(book.split()[1])
        cnt[category] += quantity

    res = []
    for cat in categories:
        res.append(f"({cat} : {cnt.get(cat, 0)})")
    return ' - '.join(res)
```

---


[Codewars link](https://www.codewars.com/kata/54dc6f5a224c26032800005c)
