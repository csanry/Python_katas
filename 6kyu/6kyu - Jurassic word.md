## Jurassic Word - 6kyu

**Instructions**

- Jurassic Word is full of wonderful prehistoric creatures eating a lot. Your task is to take in a lunchtime scene of a dinosaur and their food, and decipher exactly what ate what.

- A dino might be eating one of:

```
dead_dino = "_C     C}>"    # When this case is included in your return string, use "a dead dino" instead of "dead_dino"
flowers   = "iii     iii"
leaves    = "|||     |||"
something = "...     ..."   # for any other food you could encounter (dots being the food, in a regexp notation, all the characters in the middle being the bitemarks)
```

- These empty spaces in the middle of each food are reserved for the bitemarks made by a dinosaur, which will always be 5 characters long.

- Unfortunately, you don't get to see the action. You have to look at the bite marks made on the leftovers, and make your judgement that way.

- There are four kinds of dinosaurs in the park that you know of:

```
T-Rex = "VvvvV"
brachiosaurus = "uuuuu"
velociraptor = "vvvvv"
triceratops = "uuVuu"
```

- Although a dinosaur will be eating one of the three available foods, some dinosaurs will only eat certain items.

- For example, both the brachiosaurus and the triceratops are vegetarians and love to eat flowers, but only the brachiosaurus would be able to reach the leaves.

- On the other hand, the T-Rex and the velociraptor would only want to eat dead dinos.

- Thus, if you see their bitemarks on a food that you know they wouldn't be eating, you must be mistaken and something else is feeding.

- This is also true for bitemarks you have never seen before!

---

#### Test cases

```python
jw = JurassicWord()
print(jw.lunch_time("_CVvvvVC}>"))
print(jw.lunch_time("_CvvvvvC}>"))
print(jw.lunch_time("iiiuuVuuiii"))
print(jw.lunch_time('(((vvvvv)))'))
print(jw.lunch_time("|||uuVuu|||"))
print(jw.lunch_time("_CVvVvVC}>"))
```

#### Output

```
A T-Rex is eating a dead dino.
A velociraptor is eating a dead dino.
A triceratops is eating flowers.
A velociraptor is eating something.
Something is eating leaves.
Something is eating a dead dino.
```

---

#### Solution

```python
class JurassicWord(object):

    @classmethod
    def lunch_time(self, scene):
        dino_dict = {'vvvvv': 'A velociraptor', 'uuuuu': 'A brachiosaurus',
                     'VvvvV': 'A T-Rex', 'uuVuu': 'A triceratops'}
        food_dict = {'_CC}>': 'a dead dino.', 'iiiiii': 'flowers.', '||||||': 'leaves.'}

        dino = dino_dict.get(scene[-8:-3], 'Something')
        food = food_dict.get(scene[:-8] + scene[-3:], 'something.')
        if (food == 'a dead dino.' and dino not in ('A T-Rex', 'A velociraptor')) or\
        (food == 'leaves.' and dino != 'A brachiosaurus') or\
        (food in ('leaves.', 'flowers.') and dino not in ('A brachiosaurus', 'A triceratops')):
            dino = 'Something'

        return f'{dino} is eating {food}'
```

---

[Codewars link](https://www.codewars.com/kata/55709dc15ebd283cc9000007)
