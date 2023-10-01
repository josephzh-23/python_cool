from itertools import combinations, permutations

# the number of 3 even digits here a little bit more advanced here

#

# let's try with the combinatinos

digits = [2, 1, 3, 0]
# sounds good here
value = permutations(digits,3)
#the combinations function return an iterator here, we can loop thru the iterator to get
# results or convert it into a list
ans = list(value)

# convert to a list first and then the line here

for num in ans:
    joined = ''.join(str(x) for x in num)
    print(joined)