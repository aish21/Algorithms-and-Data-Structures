# Python implementation of Binary Tree

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.inOrder()
    
    def preOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
    
    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.val, end=' ')

# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.preOrder()
print("\nIn order Traversal: ", end="")
root.inOrder()
print("\nPost order Traversal: ", end="")
root.postOrder()
        
        
