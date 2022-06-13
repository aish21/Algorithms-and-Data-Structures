'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def inorder_fn(tree):
            if tree:
                inorder_fn(tree.left)
                output.append(tree.val)
                inorder_fn(tree.right)
        
        inorder_fn(root)
        
        return output