x = set(['foo', 'bar', 'foo', 'qux'])

x = {'foo', 'bar', 'baz', 'foo', 'qux'}


# how to work with list of lists in python
# a set of lists right here
y = set()
# can also be done above with the function literal as said

y.add((3, 4))
print(y)

# to check if in the set you can do
if (3, 4) in y:
    print("yes already included")