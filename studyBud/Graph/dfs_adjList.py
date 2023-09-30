# this will be using the dfs here
from collections import defaultdict


class Graph:
    def __init__(s):
        s.graph = defaultdict(list)

    # these are the 2 edges here
    def addEdge(s, u, v):
        s.graph[u].append(v)

    def dfsUtil(s, v, visited):

        # mark current node as viisted
        visited.add(v)
        print(v, end = ' ')

        for neigh in s.graph[v]:
            if neigh not in visited:
                s.dfsUtil(neigh, visited)

        # The function to do DFS traversal. It uses
        # recursive DFSUtil()

    def dfs(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.dfsUtil(v, visited)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2)")

    # Function call
    g.dfs(2)