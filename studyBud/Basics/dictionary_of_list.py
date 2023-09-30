from collections import defaultdict

from studyBud.Graph.dijkstra.cheapest_flight import flights

#working with a map of lists here
nums = [1, 2, 3, 4,5]
map = defaultdict()
for num in nums:
    if num in map:
        map[num] += 1
    else:
        map[num] = 1



graph = defaultdict(list)

# store the number of stops for that node here
numOfStops = {}
for flight in flights:
    start, dest, price = flight

    graph[start].append([dest, price])
