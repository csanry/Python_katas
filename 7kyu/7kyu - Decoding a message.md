## Decoding a message - 7kyu

**Instructions**

- You have managed to intercept an important message and you are trying to read it.

- You realise that the message has been encoded and can be decoded by switching each letter with a corresponding letter.

- You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.

- For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc.

- Create a function that will instantly decode an encoded message.

- You can assume no punctuation or capitals, only lower case letters, but remember spaces.

---

#### Test cases

```python
print(decode("svool"))
print(decode("r slkv mlylwb wvxlwvh gsrh nvhhztv"))
print(decode("gsv vrtsgs hbnkslmb dzh qvzm hryvorfh urmzo nzqli xlnklhrgrlmzo kilqvxg lxxfkbrmt srn rmgvinrggvmgob"))
print(decode("husbands ask repeated resolved but laughter debating"))
print(decode(" "))
print(decode(""))
```

#### Output
```
hello
i hope nobody decodes this message
the eighth symphony was jean sibelius final major compositional project occupying him intermittently
sfhyzmwh zhp ivkvzgvw ivhloevw yfg ozftsgvi wvyzgrmt
" "
""
```

---

#### Solution

```python
from string import ascii_lowercase
def decode(message):
    return message.translate(str.maketrans(ascii_lowercase, ascii_lowercase[::-1]))
```

---

[Codewars link](https://www.codewars.com/kata/565b9d6f8139573819000056)
