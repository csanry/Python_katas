## Hex Cipher - 6kyu

**Instructions**

- Implement methods `encode` and `decode` of class `HexCipher`, which applies the ASCII to hexadecimal conversion `n` times.

---

#### Test cases

```python
print(HexCipher.encode('Hey guys', 1))
print(HexCipher.decode('4865792067757973', 1))
print(HexCipher.encode('Hey guys', 2))
print(HexCipher.decode('34383635373932303637373537393733', 2))
```

#### Output 

```
4865792067757973
Hey guys
34383635373932303637373537393733
Hey guys
```

---

#### Solution

```python
TEXT2HEX = {'\x0c': '0c', 'l': '6c', 'm': '6d', 'T': '54', 'w': '77', 'y': '79', '>': '3e', '/': '2f', 'Y': '59', 
            'h': '68', 'j': '6a', 'c': '63', 'E': '45', 'F': '46', '%': '25', '\n': '0a', 's': '73', 't': '74', 
            '?': '3f', 'L': '4c', '<': '3c', 'H': '48', ':': '3a', 'N': '4e', '&': '26', 'r': '72', 'J': '4a', 
            'b': '62', '$': '24', 'd': '64', 'I': '49', 'q': '71', '=': '3d', 'Q': '51', '(': '28', 'a': '61', 
            '}': '7d', '7': '37', 'R': '52', '#': '23', 'A': '41', 'Z': '5a', 'x': '78', ';': '3b', '\t': '09', 
            '*': '2a', 'e': '65', '\r': '0d', 'P': '50', '0': '30', '{': '7b', 'C': '43', 'O': '4f', '\x0b': '0b', 
            '2': '32', 'z': '7a', ',': '2c', 'B': '42', '|': '7c', 'W': '57', 'G': '47', 'V': '56', "'": '27', 
            '4': '34', '!': '21', 'v': '76', '6': '36', '^': '5e', '3': '33', 'K': '4b', ')': '29', '.': '2e', 
            '-': '2d', 'g': '67', '5': '35', '8': '38', 'S': '53', 'D': '44', '~': '7e', 'k': '6b', '@': '40', 
            '9': '39', '[': '5b', 'p': '70', 'f': '66', 'M': '4d', 'X': '58', '1': '31', ' ': '20', 'o': '6f', 
            '_': '5f', 'i': '69', '\\': '5c', 'U': '55', ']': '5d', 'n': '6e', '`': '60', '"': '22', '+': '2b', 
            'u': '75'}
```

```python
HEX2TEXT = {v: k for k, v in TEXT2HEX.items()}

class HexCipher:

    @classmethod
    def encode(cls, mes, n):
        for _ in range(n): 
            mes = ''.join(TEXT2HEX[let] for let in mes)
        return mes
        
    @classmethod
    def decode(cls, mes, n):
        for _ in range(n): 
            mes = ''.join(HEX2TEXT[mes[i:i+2]] for i in range(0, len(mes), 2))
        return mes
```

---

[Codewars link](https://www.codewars.com/kata/59c191df4f98a8a70b00001e)
