from itertools import combinations, permutations

# the number of 3 even digits here a little bit more advanced here

#

# let's try with the combinatinos

digits = [2, 1, 3, 0]
value = permutations(digits,3)

ans = list(value)

# convert to a list first and then the line here


final = []
tests = []
for num in ans:
    joined = ''.join(str(x) for x in num)
    tests.append(joined)


    # once you get joined
print(tests)
for i in range(len(tests)):
    count1 = 0

    # exclude all the ones with leading 0 as indiciated in the question
    if(tests[i][0] == '0'):
        continue

    original = int(tests[i])

    print(f'original is {original}')
    tests[i] = int(tests[i])

    # this will then be an even number
    if tests[i] % 2 ==0:
        final.append(tests[i])

print(final)