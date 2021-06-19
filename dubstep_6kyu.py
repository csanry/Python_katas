# dubstep - 6kyu

'''
Let's assume that a song consists of some number of words (that don't contain WUB).
To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB"
1. Before the first word of the song (the number may be zero)
2. After the last word (the number may be zero)
3. Between words (at least one between any pair of neighbouring words)

For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

Given:
The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters.

Return:
The words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
'''

def song_decoder(song):
    return ' '.join(song.replace('WUB', ' ').split())

print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))