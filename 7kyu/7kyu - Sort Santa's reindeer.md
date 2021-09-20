## Sort Santa's Reindeer - 7kyu

**Instructions**

- Write a function that accepts a sequence of Reindeer names, and returns a sequence with the Reindeer names sorted by their last names.

---

#### Test cases

```python
print((sort_reindeer(['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada']))
print((sort_reindeer([]))
print((sort_reindeer(['Yasuo Kodai', 'Kenjiro Sado', 'Daisuke Aihara', 'Susumu Shima', 'Akira Sanada', 'Yoshikazu Okita', 'Shiro Yabu', 'Sukeharu Nanbu', 'Sakezo Yamamoto', 'Hikozaemon Ohta', 'Juzo Mori', 'Saburo Tokugawa']))
print((sort_reindeer(['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']))
print((sort_reindeer(["Sukeharu Yamamoto", "Juzo Yabu", "Saburo Shima", "Shiro Sanada", "Daisuke Mori"]))
```

#### Output 
```
['Kenjiro Mori', 'Juzo Okita', 'Akira Sanada', 'Susumu Tokugawa']
[]
['Daisuke Aihara', 'Yasuo Kodai', 'Juzo Mori', 'Sukeharu Nanbu', 'Hikozaemon Ohta', 'Yoshikazu Okita', 'Kenjiro Sado', 'Akira Sanada', 'Susumu Shima', 'Saburo Tokugawa', 'Shiro Yabu', 'Sakezo Yamamoto']
['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']
['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']
```

---

#### Solution

```python
def sort_reindeer(reindeer_names: list):
    return sorted(reindeer_names, key = lambda x: x.split()[1])
```

---

[Codewars link](https://www.codewars.com/kata/52ab60b122e82a6375000bad)
