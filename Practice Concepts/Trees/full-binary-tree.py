# Python implementation of checking for full binary tree

class Node:
    def __init__(self, item):
        self.leftC = None
        self.rightC = None
        self.item = item

def isFullBinaryTree(root):
    
    # Empty Tree
    if root is None:
        return True
    
    if root.leftC is None and root.rightC is None:
        return True
    
    if root.leftC is not None and root.rightC is not None:
        return isFullBinaryTree(root.leftC) and isFullBinaryTree(root.rightC)
    
    return False

# Driver Code
root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.rightChild.leftChild = Node(6)
root.leftChild.rightChild.rightChild = Node(7)

if(isFullBinaryTree(root)):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")