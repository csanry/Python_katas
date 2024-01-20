## Inverted Index - 7kyu

**Instructions**

- You are given an array of strings `coll`, a search `term`, and two booleans fine-tuning your indexing operation.

- Return an array containing the document IDs (1-based index of documents in the array) where term occurs, sorted in ascending order.

- Booleans:

```
cS (case-sensitive): test matches test, but not Test
not cS (case-sensitive): test matches both test and Test

eM (exact-match): test matches test and .test!, but not attest or test42
not eM (exact-match): test matches both test and attest
```

---

#### Test cases

```python
print(build_inverted_index(['hello there', 'gEnErAl kenobi'],'general', True, False))
print(build_inverted_index(['Lorem Ipsum Dolor', 'Hodor Dolor Hodor', 'Dolormiten are not a thing'],'Dolor', True, False))
print(build_inverted_index(['hello there', 'general kenobi'],'Hello', False, False))
print(build_inverted_index(['Rumpel Dumpel','Holger', 'Quadrumpel'],'UmPeL', False, False))
print(build_inverted_index(['hello. there', 'general kenobi'],'hello', True, True))
print(build_inverted_index(['Im Wald gibts nicht viel zu tun', 'Oooh du schoener Westerwald'],'wald', False, True))
```

#### Output

```
[]
[1, 2, 3]
[1]
[1, 3]
[1]
[1]
```

---

#### Solution

```python
import re
def build_inverted_index(coll, term, cS, eM):
    return [idx for idx, val in enumerate(coll, 1) if\
            re.search(r'{0}{1}{0}'.format('\\b' if eM else '', term), val, flags=not cS and re.I)]
```

---

[Codewars link](https://www.codewars.com/kata/5af823451839f1768f00009d)
