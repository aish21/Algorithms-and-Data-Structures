# Python implementation of binary search tree operations

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
    
# Inorder Traversal
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(str(root.key) + "->", end=' ')
        inOrder(root.right)

# Insert a node
def insertNode(node, key):
    if node is None:
        return Node(key)
    
    if key < Node.key:
        node.left = insertNode(node.left, key)
    else:
        node.right = insertNode(node.right, key)
    
    return node

# INORDER SUCCESSOR
def inOS(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Delete Node
def delNode(root, key):
    if root is None:
        return root
    
    if key < root.key:
        root.left = delNode(root.left, key)
    elif(key > root.key):
        root.right = delNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = inOS(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = delNode(root.right, temp.key)

    return root

# Driver Code
root = None
root = insertNode(root, 8)
root = insertNode(root, 3)
root = insertNode(root, 1)
root = insertNode(root, 6)
root = insertNode(root, 7)
root = insertNode(root, 10)
root = insertNode(root, 14)
root = insertNode(root, 4)

print("Inorder traversal: ", end=' ')
inOrder(root)

print("\nDelete 10")
root = delNode(root, 10)
print("Inorder traversal: ", end=' ')
inOrder(root)