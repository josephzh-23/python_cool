

# then here we have this thing that we can use

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


#TC: O (n + m)

adjList = [[2,4],[1,3],[2,4],[1,3]]

# given an list of list turn them into an adjList here

def cloneGraphBig(node):


    '''
    a dictionary to save the visited node here
    key: node of original graph
    value: corresponding cloned node

    We have to use visited otherwise would be stuck in a cycle as said
    '''

    visited = {}

    def cloneGraph(node):
        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in visited:
            return visited[node]


        #so if not visited before, let's create a clone here
        cloneNode = Node(val = node.val, neighbors = [])

        # add this to visited
        visited[node] = cloneNode

        # iterate thru the neighbor of node
        if node.neighbors:
            for neigh in node.neighbors:
                cloneNode.neighbors.append(neigh)

        return cloneNode










