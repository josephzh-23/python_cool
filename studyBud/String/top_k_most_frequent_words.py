from collections import defaultdict
import heapq as h

nums = [1, 1, 1, 2,2, 3]
# most frequent words
def topMostFrequentWords(nums, k):
    min = []
    map = defaultdict()
    for num in nums:
        if num in map:
            map[num]+=1
        else:
            map[num] = 1

    # iterate over the # fo items

    # keep k top frequen 
    for count in map.keys():
        h.heappush(min,count)
        if(len(min) > k): h.heappop(min)

    print(min)
topMostFrequentWords(nums,2)