# delete occurrences of an element if occurs more than n times - 6kyu

'''
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2].
Drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times.
Finally, take 3, which leads to [1,2,3,1,2,3].

Examples:
delete_nth ([1,1,1,1],2) => return [1,1]
delete_nth ([20,37,20,21],1) => return [20,37,21]
'''

def delete_nth(order, max_e):
    from collections import defaultdict
    cnt = defaultdict(int)
    result = []
    for element in order:
        if cnt[element] < max_e:
            result.append(element)
            cnt[element] += 1
    return result

print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))
print(delete_nth([1, 5, 5, 5, 5, 5, 5, 5, 1, 37, 5, 5],5))