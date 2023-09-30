from itertools import combinations

from print_list import printList

# for building the combination here


value = combinations(["james", "home", "map"],2)
#the combinations function return an iterator here, we can loop thru the iterator to get
# results or convert it into a list
print(list(value))
# printList(value)

