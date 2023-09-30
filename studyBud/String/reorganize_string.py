

# here we can reorganize the strign right here

'''
https://leetcode.com/problems/reorganize-string/
TC: O(nlogn)

Use a max heap-> b/c most frequent item here
1. this would mean O (logn)
2. can replace sorting for us

start with the most freq char
Use a hashmap

a -> 3      b -> 2     c -> 2

each time we take off a, also then take off b, since this is the next most
freq elemetn
a: 3      a: 2      a: 1
b: 1 ->   b: 0  ->  b: 0
c: 1      c: 1      c: 0

Each time a letter is used, use a diff character
so use a previous to keep track of pointer

'''
import heapq
from collections import Counter

s = "sdfsf"
def reorganizeString(word, s: str):

    # better then doing a for loop and then
    count = Counter(s)
    maxHeap = [[-cnt, char] for char, cnt in count.items()]

    heapq.heapify(maxHeap)

    #then right here we have the right code
    #store the previous character we built














