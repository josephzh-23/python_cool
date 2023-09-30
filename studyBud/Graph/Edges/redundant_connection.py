from typing import List

from print_list import printList

'''
Step 1:
For each edge, check if the nodes it connects are 
already connected by calling the union() method of the 
UnionFind instance with the two nodes as arguments.

1. 
If nodes are connected, current edge creates a cycle in the grpah here 

2. If not connected then calling union() will then connect them as said 

3. If no redundant connection are found then return the edge that was found here 

'''


# the problem here is that the redundant edge will link together an already linked together
# grpah as said here

# use union and find to see if sth has alread ybeen linked together or not
def redundantConnection(edges: List[List[int]]) :

    n = len(edges)

    # all parents will be 1 for now
    parent = [1] * (n + 1)

    # Find the ancestor of each node here
    def find(node):
        node = node
        while parent[node] != node:
            node = parent[node]
        return node


    def union(i, j):
        iRoot = find(i)
        jRoot = find(j)

        #only perform union if not the same as said before
        # and tehn we have some data points to play with here right her e
        if( iRoot != jRoot):
            parent[jRoot] = iRoot

    for node1, node2 in edges:

        # if ancestors are the same then return that edge
        if(find(node1) == find(node2)): return [node1, node2]

        # Else just keep reunioning this as said
        union(node1, node2)
    return

edges = [[1, 2], [2,3], [3, 4], [1, 4], [1, 5]]

# Now we run the code over here
print(redundantConnection(edges))













    # using this you could have a bunch of data that could make some sense
    # and then