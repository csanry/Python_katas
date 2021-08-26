## Drunk Friend - 6kyu

**Instructions**

You're hanging out with your friends in a bar, when suddenly one of them is so drunk, that he can't speak, and when he wants to say something, he writes it down on a paper. However, none of the words he writes make sense to you. He wants to help you, so he points at a beer and writes "yvvi". You start to understand what he's trying to say, and you write a script, that decodes his words.

- Keep in mind that numbers, as well as other characters, can be part of the input, and you should keep them like they are. 

- You should also test if the input is a string. 

- If it is not, return "Input is not a string".


---

#### Test cases

```python
print(decode("yvvi"))
print(decode("Blf zoivzwb szw 10 yvvih"))
print(decode("Ovg'h hdrn rm gsv ulfmgzrm!"))
print(decode("Tl slnv, blf'iv wifmp")) 
```

#### Output 
```
beer
You already had 10 beers
Let's swim in the fountain!
Go home, you're drunk
```

---

#### Solution

```python
def decode(s):
    trans = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    drunk = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
    return s.translate(str.maketrans(drunk, trans)) if type(s) == str else 'Input is not a string'
```

---


[Codewars link](https://www.codewars.com/kata/558ffec0f0584f24250000a0)
