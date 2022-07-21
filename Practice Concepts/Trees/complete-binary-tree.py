# Python implementation for checking if complete binary tree

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

# Count number of nodes
def numNodes(root):
    if root is None:
        return 0
    return (1 + numNodes(root.left) + numNodes(root.right))

# Check whether it is complete binary tree
def isCompleteTree(root, index, numnodes):
    if root is None:
        return True
    
    if index >= numnodes:
        return False
    
    return (isCompleteTree(root.left, 2 * index + 1, numnodes)
            and isCompleteTree(root.right, 2 * index + 2, numnodes))

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = numNodes(root)
index = 0

if isCompleteTree(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")