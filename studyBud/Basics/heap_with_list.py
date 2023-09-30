import heapq as h
from collections import Counter


# using this here would really help

def reorganizeString(word, s: str):

    # better then doing a for loop and then
    count = Counter(s)
    heap = [[-cnt, char] for char, cnt in count.items()]
    h.heapify(heap)

    res = []
    while len(heap) >=2:
        topCount, topChar = h.heappop(heap)
        nextCount, nextChar = h.heappop(heap)

        res.append(topChar)
        res.append(nextChar)

        #check if the topCount == 0, if it is it means this is used up here
        if topCount +1 !=0:
            h.heappush(heap, [topCount+ 1, topChar])

        if nextCount + 1 !=0:
            h.heappush(heap, [nextCount + 1, nextChar])



    if heap:

        # so here we have to make sure the top character != the last character we added
        # here
        topCount, topChar = h.heappop(heap)

         # if [a, b]  the top char is b this case will not work
        # or if there is still sth left -1
        if topCount != -1 or topChar == res[-1]:
            return ""

        else:
            res.append(topChar)

    return "".join(res)