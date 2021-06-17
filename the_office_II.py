'''

Every now and then people in the office moves teams or departments.
Depending what people are doing with their time they can become more or less boring.
Time to assess the current team.

You will be provided with an object(staff) containing the staff names as keys and department they work in as values.
Each department has a different boredom assessment score, provided in the dictionary.

'''

def boredom(staff):
    boredom_scores = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25,
    }
    score = sum(map(boredom_scores.get, staff.values()))
    return (
        'kill me now' if score <= 80 else
        'i can handle this' if score < 100 else
        'party time!!')

print(boredom({'a': 'change', 'b': 'cleaning'}))
print(boredom({'a': 'pissing about', 'b': 'pissing about', 'c': 'pissing about', 'd': 'pissing about'}))
