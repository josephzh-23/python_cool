# performing the bfs search here might be good down the road here


"""
you might have several lines here
"""
from print_list import printList

graph = {
    '5': ['3', '7'],
    '3':['2', '4'],
    '7': ['8'],
    '2': [],
    '4':['8'],
    '8':[]
}

visited = []        #list for visited nodes here
q = []              # init a queue

def bfs(visited, graph, node): #functino for bfs
    visited.append(node)
    q.append(node)

    while q:
        s = q.pop(0)
        # print(s, end = " ")

        # this will then print out all the neighbors very intersting 
        for neigh in graph[s]:

            if neigh not in visited:
                visited.append(neigh)
                q.append(neigh)
                print("q is " +printList(q))

bfs(visited, graph, '5')




















