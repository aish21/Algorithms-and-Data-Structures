# Python implementation of tree traversal 

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item
    
def inOrder(root):

    if root:
        # Traverse the left subtree
        inOrder(root.left)
        # Traverse the root
        print(str(root.val) + "->", end='')
        # Traverse the right subtree
        inOrder(root.right)

def preOrder(root):
    if root:
        # Traverse the root
        print(str(root.val) + "->", end='')
        # Traverse the left subtree
        preOrder(root.left)
        # Traverse the right subtree
        preOrder(root.right)

def postOrder(root):
    if root:
        # Traverse the left subtree
        postOrder(root.left)
        # Traverse the right subtree
        postOrder(root.right)
        # Traverse the root
        print(str(root.val) + "->", end='')

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inOrder(root)

print("\nPreorder traversal ")
preOrder(root)

print("\nPostorder traversal ")
postOrder(root)