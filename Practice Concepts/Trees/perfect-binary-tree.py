# Python implementation for checking if perfect binary tree

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.key = item

# Depth Calculation
def depth(node):
    d = 0
    while node is not None:
        d += 1
        node = node.left
    return d

# Check is perfect binary tree
def isPerfectBinaryTree(root, d, level = 0):
    if root is None:
        return True
    
    if(root.left is None and root.right is None):
        return (d == level + 1)
    
    if(root.left is None or root.right is None):
        return False
    
    return (isPerfectBinaryTree(root.left, d, level + 1) and
            isPerfectBinaryTree(root.right, d, level + 1))

# Driver code
root = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if (isPerfectBinaryTree(root, depth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
