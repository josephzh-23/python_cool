from studyBud.Binary_Search_Tree.BFS_rec import Node


# preOrder
#  Preorder (Root, Left, Right) : 1 2 4 5 3


def preOrderRec(r):

    if r:
        print(r.val)
        preOrderRec(r.left)
        preOrderRec(r.right)



'''

This means root comes before all its children is what it means 
    1
  2   3
4   5
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
'''
# root, left and right, this is the exact opposite of printLevelOrder()
def PreorderIter(root):
    # Base CAse
    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.val, end=" ")

        if node.right:
            # print('right val', node.right.val, end=" ")
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# PreorderIter(root)