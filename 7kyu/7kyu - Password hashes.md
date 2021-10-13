## Password hashes - 7kyu

**Instructions**

- When you sign up for an account somewhere, some websites do not actually store your password in their databases. 

- Instead, they will transform your password into something else using a cryptographic hashing algorithm.

- After the password is transformed, it is then called a password hash. 

- Whenever you try to login, the website will transform the password you tried using the same hashing algorithm and simply see if the password hashes are the same.

- Create the function that converts a given string into an `md5` hash. 

- The return value should be encoded in `hexadecimal`.

```
passHash("password") // --> "5f4dcc3b5aa765d61d8327deb882cf99"
passHash("abc123") // --> "e99a18c428cb38d5f260853678922e03"
```

---

#### Test cases

```python
print(pass_hash('password'))
print(pass_hash('abc123'))
```

#### Output 

```
5f4dcc3b5aa765d61d8327deb882cf99
e99a18c428cb38d5f260853678922e03
```

---

#### Solution

```python
import hashlib
def pass_hash(st):
    return hashlib.md5(st.encode()).hexdigest()
```

---

[Codewars link](https://www.codewars.com/kata/54207f9677730acd490000d1)
