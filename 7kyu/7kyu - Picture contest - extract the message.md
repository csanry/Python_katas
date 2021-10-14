## Picture Contest - Extract the message - 7kyu

**Instructions**

- Implement a function that takes out the hashtag from the posted message. 

- When multiple occurrences of the hashtag are found, delete only the first one.

- Where the hashtag isn't present, the message should in this case stay untouched.

- The hashtag only consists of alphanumeric characters.

```
* ("Sunny day! #lta #vvv", "#lta") -> "Sunny day!  #vvv" (notice the double space)
* ("#lta #picture_contest", "#lta") -> " #picture_contest"
```

---

#### Test cases

```python
print(omit_hashtag("Sunny day! #lta #vvv", "#lta"))
print(omit_hashtag("#lta #picture_contest", "#lta"))
print(omit_hashtag("#lta #picture_contest #lta", "#lta"))
```

#### Output 

```
Sunny day!  #vvv
 #picture_contest
 #picture_contest #lta
```

---

#### Solution

```python
def omit_hashtag(message, hashtag):
    return message.replace(hashtag, '', 1)
```

---

[Codewars link](https://www.codewars.com/kata/5a06238a80171f824300003c)
