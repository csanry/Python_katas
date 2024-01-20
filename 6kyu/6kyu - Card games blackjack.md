## Card Games: Black Jack - 6kyu

**Instructions**

- Your assignment is to complete the function that draws cards for the dealer, and returns the players who have won.

- Each table will consist of 3 players, `p1`, `p2`, `p3`.

- Players play against the `dealer` only, not against other players.

- Each card has its value: the numerals are worth whatever their number indicates; `J`, `Q` and `K` are worth 10; `A` may be worth 11 or 1.

- If any player exceeds 21 points, they lose.

- The dealer must draw from a deck until it's hand scores 17 or more points.

- A player has a blackjack when they have 2 cards, one worth `10`, and an `A`

- If the player has a blackjack, then they win, unless the dealer also has a blackjack.

- When the dealer draws a card, the dealer draws the first card from a deck.

---

#### Test cases

```python
print(winners(
    ["6", "A", "2", "Q", "3"], #22
    ["5", "8"],                #13
    ["6", "Q", "2"],           #18
    ["3", "10"],               #14, 18 after drawing
    ["A", "4", "10", "5", "4", "A", "Q", "2", "6", "A", "5", "7", "9", "Q", "2", "8", "9", "A", "K", "2", "8"]))
print(winners(
    ["J", "A"],                # 21 BJ
    ["8", "J", "7"],           # 25
    ["2", "4", "K", "10"],     # 26
    ["K", "8"],                # 18, 21 after drawing
    ["3", "6", "A", "8", "9", "A", "3", "Q", "5", "2", "3", "8", "6", "J", "K", "2", "8", "7", "7", "K", "Q"]))
print(winners(
    ["J", "2", "K"],           # 22
    ["A", "5", "A", "5", "7"], # 19
    ["J", "A"],                # 21 BJ
    ["2", "Q"],                # 16, 26 after drawing
    ["4", "10", "Q", "K", "2", "8", "9", "8", "9", "4", "K", "7", "10", "A", "4", "9", "5", "A", "Q", "Q", "3"]))
```

#### Output

```
[]
['Player 1']
['Player 2', 'Player 3']
```

---

#### Solution

```python
def score(hand):
    score = sum(int(c) if c.isdigit() else 11 if c == 'A' else 10 for c in hand)
    aces = hand.count('A')

    for _ in range(aces):
        if score > 21:
            score -= 10
    return 'BJ' if score == 21 and len(hand) == 2 else score if score <= 21 else 0

def winners(p1, p2, p3, dealer, deck):
    s1, s2, s3, sd = map(score, (p1, p2, p3, dealer))

    res = []
    if sd == 'BJ':
        return res

    while 0 < sd < 17 and deck:
        dealer.append(deck.pop(0))
        sd = score(dealer)

    if s1 == 'BJ' or s1 > sd:
        res.append('Player 1')
    if s2 == 'BJ' or s2 > sd:
        res.append('Player 2')
    if s3 == 'BJ' or s3 > sd:
        res.append('Player 3')
    return res
```

---

[Codewars link](https://www.codewars.com/kata/5bebcbf2832c3acc870000f6)
