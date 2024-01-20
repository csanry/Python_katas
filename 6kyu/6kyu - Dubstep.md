## Dubstep - 6kyu

**Instructions**

- Let's assume that a song consists of some number of words (that don't contain WUB).
To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB"

    - Before the first word of the song (the number may be zero)
    - After the last word (the number may be zero)
    - Between words (at least one between any pair of neighbouring words)

- For example, a song with words `"I AM X"` can transform into a dubstep remix as `"WUBWUBIWUBAMWUBWUBX"` and cannot transform into `"WUBWUBIAMWUBX"`

- Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed.

- Help Jonny restore the original song.

**Input**

A single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters.

**Output**

The words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

---

#### Test cases

```python
song_decoder("AWUBBWUBC")
song_decoder("AWUBWUBWUBBWUBWUBWUBC")
song_decoder("WUBAWUBBWUBCWUB")
```

#### Output

```
"A B C" # WUB should be replaced by 1 space
"A B C" # multiples WUB should be replaced by only 1 space"
"A B C" # heading or trailing spaces should be removed"
```

---


```python
def song_decoder(song):
    return ' '.join(song.replace('WUB', ' ').split())
```

---

[Codewars link](https://www.codewars.com/kata/551dc350bf4e526099000ae5)
