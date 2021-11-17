## Vowel Changer - 7kyu

**Instructions**

- Create a function that changes all the vowels (excluding y) in a string, and changes them all to the same vowel. 

- The first parameter of the function is the string, and the second is the vowel that all the vowels in the string are being changed to.

- There will never be an uppercase letter as an input.

---

#### Test cases

```python
print(vowel_change("hannah hannah bo-bannah banana fanna fo-fannah fee, fy, mo-mannah. hannah!" ,'i'))
print(vowel_change('adira wants to go to the park', 'o'))
```

#### Output 

```
hinnih hinnih bi-binnih binini finni fi-finnih fii, fy, mi-minnih. hinnih!
odoro wonts to go to tho pork
```

---

#### Solution

```python
import re 
def vowel_change(txt, vow):
    return re.sub(r'[aeiou]', vow, txt)
```

---

[Codewars link](https://www.codewars.com/kata/597754ba62f8a19c98000030)
