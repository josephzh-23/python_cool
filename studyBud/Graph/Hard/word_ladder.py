from collections import defaultdict, deque
from typing import List


# we know all the words will be the same length but
# find all the adjacency words here
# find just 1 letter away here

# check if is 1 letter different?
def oneChar(s, t):
    if s == t: return False

    cnt = 0

    for i in range(len(s)):
        if s[i] != t[i]:
            cnt +=1
    return cnt ==1


alpha = "abcdefghijklmpopqrstuvwxyz"

def ladderLength(beginWord, endWord, wordList: List[str]):
    # write a functino to check if one word difference here
    graph = defaultdict(set)

    # have a bunch of sets here

    #
    wordset = set(wordList + [beginWord])
    for s in wordList + [beginWord]:
        for i in range(len(s)):
            p1, p2 = s[0: i], s[i+ 1:]

            for a in alpha:
                tmp = p1 + a + p2
                if tmp in wordset and tmp == s:
                    graph[s].add(tmp)

    # this will be out of time complexity range right here
    # the in efficient solutino here
    for s in wordList + [beginWord]:
        for t in wordList + [beginWord]:
            if oneChar(s, t):
                graph[s].add(t)


    print(graph)
    visited = []  # list for visited nodes here
    q = []  # init a queue


    node = beginWord
    visited.append(node)

    q = deque()
    q.append([beginWord, 0])
    while q:
        node, step = q.popleft()

        if node == endWord:
            # we want the total length here, not just the steps here
            return step + 1

        # this will then print out all the neighbors very intersting
        for neigh in graph[node]:
            if neigh not in visited:
                visited.append(neigh)
                q.append([neigh, step + 1])

    return 0
# Based on the above we can build sth like the following:

# The above would give us below:
'''
{'hot': {'dot', 'lot'}, 
 'dot': {'dog', 'lot', 'hot'},
  and so forth here 
'''
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]


ans = ladderLength("hot", "cog", wordList)
print(ans)




