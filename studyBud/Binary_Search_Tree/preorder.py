#this is O(n) based : # of nodes here

def preOrder(root):

    # No need for the return conditino here since we have what it takes around here
    if root:
        # First print the data of node
        print(root.val, end=" "),

        # Then recur on left child
        preOrder(root.left)

        # Finally recur on right child
        preOrder(root.right)
