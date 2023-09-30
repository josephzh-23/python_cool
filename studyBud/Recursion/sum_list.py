
# return a list of sums here using this
def listSum(numList):
    if len(numList) == 1:
        return numList[0]

    else:
        # each time this increases by 1 spot
        print(numList[0])
        return numList[0] + listSum(numList[1:])


print(listSum([2, 4, 5, 6, 7]))
