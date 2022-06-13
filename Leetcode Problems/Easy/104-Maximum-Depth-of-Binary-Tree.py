'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Recursion
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
        
        # Iteration
        '''
        stack = []
        if root is not None:
            stack.append((1, root))
        depth = 0
        while stack != []:
            current_dep, root = stack.pop()
            if root is not None:
                depth = max(depth, current_dep)
                stack.append((current_dep + 1, root.left))
                stack.append((current_dep + 1, root.right))
        return depth
        '''