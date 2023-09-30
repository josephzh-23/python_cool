import heapq
from collections import defaultdict
from itertools import combinations

username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

# so to go from joe -> home at time 1
# go from joe -> about at time 2


def mostVisitedPattern(username, timestamp, website):

    TUW = tuple(zip(timestamp, username, website))
    sortedTUW = sorted(TUW)

    # the above will then be sorted by the time as said
    '''
    [(1, 'joe', 'home'), 
     (2, 'joe', 'about'), (3, 'joe', 'career')
     '''


    #then use sth to build the user history here
    userHistory = defaultdict(list)


    for _, user, website in sortedTUW:
        userHistory[user].append(website)

    # 'james' : ['home', 'cart', 'maps', 'home]
    patternCount = defaultdict(int)

    # we want to create a combinatino of user values
    # so ex: if the value is ['home', 'cart', 'maps','home']
    # using the combination(, 3) below convert that to make sure it's kind of like
    # ['home', 'cart', 'maps', 'home']
    for user in userHistory.keys():

        # turn the iterator of combinations into a list here
        combs = set(combinations(userHistory[user], 3))
        print(combs)
        for comb in combs:
            patternCount[comb] = patternCount[comb] + 1


    # this gives you all the count of each pattern
    a = [-x for x in patternCount.values()]
    b = patternCount.keys()

    c = list(zip(a, b))
    heapq.heapify(c)
    return heapq.heappop(c)[1]

    # def sortKey(pattern):
    #     return (-patternCount[pattern], pattern)


mostVisitedPattern(username, timestamp, website)
