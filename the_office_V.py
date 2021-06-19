# the office V, 6kyu

'''
You need x chairs - specified by the need argument

Find the spare chairs from the array of meeting rooms.
Each meeting room object will have the number of occupants as a string.
Each occupant is represented by 'X'.
The room object will also have an integer telling you how many chairs there are in the room.

Return an array of integers that shows how many chairs you take from each room in order.
Only take up to the required amount.
If you need no chairs: return "Game On!"
If there are insufficient chairs, return "Not Enough!"
'''

def meeting(rooms, need):
    if need == 0:
        return "Game On!"

    result = []
    for people, chairs in rooms:
        taken = min( max(chairs - len(people), 0), need )
        result.append(taken)
        need -= taken
        if need == 0:
            return result
    return "Not Enough!"

assert meeting([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4) == [0, 1, 3]







