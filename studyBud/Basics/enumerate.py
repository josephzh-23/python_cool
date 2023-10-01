l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)


# enumearte si kind of like the forEachIndexed
print("Return type:", type(obj1))
print(list(enumerate(l1)))

# will count sth like the above
'''
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
'''

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))