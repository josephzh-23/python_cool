from studyBud.Binary_Tree.binaryTree import BinaryNode


# Ok here


# can also do this wile using traversal
def maxDepth(node):

    if node is None:
        return 0

    else:
        lDepth = maxDepth(node.left)
        print(lDepth)
        rDepth = maxDepth(node.right)

        if lDepth > rDepth:
            return lDepth + 1

        else:
            return rDepth + 1

root = BinaryNode(1)
root.left = BinaryNode(2)
root.right = BinaryNode(3)
root.left.left = BinaryNode(4)
root.left.right = BinaryNode(5)

print('height of the tree is %d' %maxDepth(root))