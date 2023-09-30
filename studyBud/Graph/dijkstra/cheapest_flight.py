import heapq as h
from collections import defaultdict

# cheapest
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0; dst = 3; k = 1

# flight from 0 -> 1 100 dollars, want the cheapest one here

# number of flights here

def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(list)

    # store the number of stops for that node here
    numOfStops = {}
    for flight in flights:
        start, dest, price = flight

        graph[start].append([dest, price])

    print(graph)

    # the price, source, # of stops here from source node
    pq = [[0, src, 0]]
    while pq:
        cost, node, stops = h.heappop(pq)

        if(node == dst) and stops -1 <=k:
            return cost

        # we have encountered sth with smaller # of stops
        if node not in numOfStops or numOfStops[node] >stops:
            '''
                  Need to store the number of steps for that node in particular here
                 SO no more processing if sth similar occurs here
                 '''
            numOfStops[node] = stops
            for neigh, price in graph[node]:
                h.heappush(pq, [cost + price, neigh, stops + 1])

    return -1
print(findCheapestPrice(n,flights, src, dst, k))
















