
'''
O(n^2) TC
Input: inorder[] = {5, 10, 40, 30, 28}
Output: root of following tree
         40
       /   \
      10     30
     /         \
    5          28

the maximum will be 40 will be the root
and build from left and build from right

# So here need to find the maximum value here
which will be the root
'''
from studyBud.Binary_Search_Tree.BSTNode import Node


def buildTree(array, start, end):

    if start > end:
        return None


    maxIndex = findMax(array, start, end)

    root = Node(maxIndex)

    # If this is the only element in
    # inorder[start..end], then return it
    if start == end:
        return root

    root.left = buildTree(array, start, maxIndex -1)
    root.right = buildTree(array, maxIndex+1, end)

    return root


# return the max index
def findMax(arr, start, end):
    maxValue = arr[start]
    maxIndex = start

    # need to iterate the whole thing here
    for i in range(start+1, end+1):
        if arr[i] > maxValue:
            maxValue = arr[i]
            maxIndex = i

    return maxIndex
