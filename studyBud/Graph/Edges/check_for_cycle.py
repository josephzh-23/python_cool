import collections

from print_list import printList
from studyBud.Basics.print_dictionary import printDict

# turn a list of lists into a graph adjacency here

arr = [[1, 2], [3, 4], [5, 6]]

'''
Complexity: O (V + E)
Basically 2 arrays here : parent and then the edges here 
'''

def hasCycle(numNodes, edges):
    graph = buildAdjList(numNodes, edges)
    # print("adjacency list", graph)
    print("")
    visited = set()
    for node in range(numNodes):
        print("dfs node", node)
        if node not in visited and detectCycle(graph, node, visited, None):
            return True


def detectCycle(graph, node, visited, parent):
    if node in visited:
        print("node ", node, "has been visited")
        return True

    visited.add(node)

    for descendant in graph[node]:

        # if node is different and node has been visited then a cycle here
        if descendant != parent and detectCycle(graph, descendant, visited, node):
            return True
    return False


# turn edges into adjacency list map {3: [1, 2]}
def buildAdjList(numNodes, edges):
    graph = collections.defaultdict(list)


    for edge in edges:
        a, b = edge
        # bidirection
        graph[b].append(a)
        graph[a].append(b)

    # printDict(graph)

    return graph


if __name__ == "__main__":
    numNodes = 6
    edges = [[1, 0], [3, 0], [5, 0], [2, 1], [3, 1], [4, 3], [5, 4], [3, 5]]
    print("has cycle?", hasCycle(numNodes, edges))
