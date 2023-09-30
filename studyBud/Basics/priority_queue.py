import heapq as h
customers = []
h.heappush(customers, (2, "Harry"))
h.heappush(customers, (3, "Charles"))
h.heappush(customers, (1, "Riya"))
h.heappush(customers, (4, "Stacy"))


# the one dropped will be the one with the smallest id here
while customers:
     print(h.heappop(customers))


#workign with a list here