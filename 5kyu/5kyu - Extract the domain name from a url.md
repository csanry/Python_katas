## Extract the domain name from a URL - 5kyu

**Instructions**

- Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 

```
For example:

domain_name("http://github.com/carbonfive/raygun") > "github" 
domain_name("http://www.zombie-bites.com") > "zombie-bites"
domain_name("https://www.cnet.com") > "cnet"
```

---

#### Test cases

```python
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
```

#### Output 

```
google
google
xakep
youtube
```

---

#### Solution

```python
import re
def domain_name(url):
    res = re.sub(r'(http|https)://', '', url)
    return res.split('.')[1 if 'www.' in res else 0]
```

---

[Codewars link](https://www.codewars.com/kata/514a024011ea4fb54200004b)
