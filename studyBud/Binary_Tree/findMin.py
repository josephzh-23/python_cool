from studyBud.Binary_Tree.binaryTree import BinaryNode

# use the smallest value first

# binary node here


# find the minimum value here

root = BinaryNode(1)
root.left = BinaryNode(2)
root.right = BinaryNode(3)
root.left.left = BinaryNode(4)
root.left.right = BinaryNode(5)

def findSmallest(root, temp):
    if root:

        temp = min(temp, root.data)
        # Compare current and then the temp that we had before
        print(root.data, end=" "),

        # Then recur on left child
        findSmallest(root.left, temp)

        # Finally recur on right child
        findSmallest(root.right, temp)

    else:
        print("smallest is", temp)
print(findSmallest(root, root.data))
