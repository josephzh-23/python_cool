

# then here we have some code

# this can be used in word ladder problem here

s = 'abcd'

p1, p2 = s[0: 2], s[3:]
print(p1, p2)
letterToAdd = "g"

newWord = p1 + letterToAdd + p2

print(newWord)