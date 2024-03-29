from collections import deque

from studyBud.Binary_Search_Tree.BFS_rec import Node

"""
height of tree = the level from the leaf node

height = max (height of left, height of right) +1

depth of tree = level from the root 



"""



# TC: O (n) the # of nodes in the tree
def getHeightRec(root):
    if root is None:
        return 0

    # This will keep calling until it gets to root is None and then start
    # to pop off that stck
    return 1 + max(getHeightRec(root.left), getHeightRec(root.right))


#And then using thedata here is actually a little bit better than using the
# other approach here And therefore not always better asdf
# and therefore not always

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Height of tree is", getHeightRec(root))