# here basically that
from itertools import combinations, permutations

import combination as combination

numbers = [8, 0, 5]
combos = combinations(numbers, 2)

print(list(combos))

# notice the above will create [(8, 0), (8, 5), (0, 5)]
# since the order matters in combinatinons so (0,8) is the same as
# (8, 0)   we can only use one of them here


# in permutations the order doesn't matter so
# using permutation here we have

perms = permutations(numbers, 2)
print(list(perms))

# this will have all 6 answers

#permutatino here stuff and then

