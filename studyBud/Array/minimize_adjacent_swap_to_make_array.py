import math


# the edge case that the smallest index and the largest index would
# over lap as you are swapping them over

# if you have [5, 3, 1] then you only have to do 1 less swap then

# so as above it would be like

# returning the above you have certain thigns
def minSwaps(nums)-> int:

    largest, smallest, largestIdx, smallestIdx = -math.inf, math.inf, 0,0


    for i, n in enumerate(nums):
        if n < smallest:
            smallest = n
            smallestIdx = i

        if n>= largest:
            largest= n
            largestIdx = i

    n = len(nums) -1

    # this is the magical formula here
    res = smallestIdx + (n -largestIdx)

    # the forementioned edge case before
    return res -1 if smallestIdx > largestIdx else res

