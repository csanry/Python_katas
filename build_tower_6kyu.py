# build tower - 6kyu

"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *
Example of 3 story tower:
[
  '  *  ',
  ' *** ',
  '*****'
]
"""

def tower_builder(n_floors):
    result = []

    for i in range(1, n_floors + 1):
        stars = 2 * i - 1
        spaces = n_floors - i
        result.append(f"{' ' * spaces}{'*' * stars}{' ' * spaces}")
    return '\n'.join(result)

print(tower_builder(5))
print(tower_builder(8))