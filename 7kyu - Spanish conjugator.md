## Spanish Conjugator - 7kyu

**Instructions**

- For conjugating in Spanish, we need to remove the infinitive suffix (ar, er or ir) and add the personal suffixes corresponding to the person we're talking to.

- Write a function called conjugate to return an object with all possible combinations of the Spanish verb.

```
Example: verb Caminar (to walk)
- Camino (I walk)
- Caminas (You walk)
- Camina (He walks)
- Caminamos (We walk)
- Camináis (You guys walk)
- Caminan (They walk)
Example: verb Comer (to eat)
- Como (I eat)
- Comes (You eat)
- Come (He, She eats)
- Comemos (We eat)
- Coméis (You guys eat)
- Comen (They eat)
Example: verb Vivir (to live)
- Vivo (I live)
- Vives (You live)
- Vive (He, She lives)
- Vivimos (We live)
- Vivís (You guys live)
- Viven (They live)
```

---

#### Test cases

```python
print(conjugate("caminar"))
print(conjugate("comer"))
print(conjugate("vivir"))
```

#### Output 
```
{'caminar': ['camino', 'caminas', 'camina', 'caminamos', 'caminais', 'caminan']}
{'comer': ['como', 'comes', 'come', 'comemos', 'comeis', 'comen']}
{'vivir': ['vivo', 'vives', 'vive', 'vivimos', 'vivis', 'viven']}
```

---

#### Solution

```python
def conjugate(verb):
    s = {'ar': 'o as a amos ais an'.split(),
         'er': 'o es e emos eis en'.split(),
         'ir': 'o es e imos is en'.split()}
    return {verb: [verb[:-2] + suffix for suffix in s[verb[-2:]]]}       
```

---

[Codewars link](https://www.codewars.com/kata/5a81b78d4a6b344638000183)
