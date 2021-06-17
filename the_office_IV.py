'''
Your job at your company is both boring and difficult.
It isn't made any easier by the fact that everyone wants a meeting with you, and that the meeting rooms are always taken!

In this kata, you will be given an array. Each value represents a meeting room.
Your job? Find the first empty one and return its index (N.B. There may be more than one empty room in some test cases).

If all rooms are busy, return "None available!"
'''

def meeting(rooms):
    for i in range(len(rooms)):
        if rooms[i] == 'O':
            return i
    return "None available!"

print(meeting(['X', 'O', 'X', 'O']))
print(meeting(['X', 'X', 'X', 'X']))