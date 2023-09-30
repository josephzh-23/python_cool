

# a binary tree: a strcuture in which every node has at most 2 children

class BinaryNode:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = BinaryNode(10)
root.PrintTree()

# this is called the binary tree right here