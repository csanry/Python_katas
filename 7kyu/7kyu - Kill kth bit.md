## Kill kth bit - 7kyu

**Instructions**

- Write a function that will change the kth bit of n (from the right) back to 0.

- If the bit is already 0, leave it as 0.

- Return the corresponding number from the transformed binary code.

---

#### Test cases

```python
print(kill_kth_bit(37,3))
print(kill_kth_bit(37,4))
print(kill_kth_bit(0,4))
print(kill_kth_bit(2147483647,16))
print(kill_kth_bit(374823748,13))
print(kill_kth_bit(1084197039,15))
```

#### Output

```
33
37
0
2147450879
374819652
1084197039
```

---

#### Solution

```python
def kill_kth_bit(n, k):
    if len(bin(n)) > k:
        return n if bin(n)[-k] == '0' else n - 2**(k-1)
    return n
```

---

[Codewars link](https://www.codewars.com/kata/58844f1a76933b1cd0000023/)
