'''
The height helps us measure the depth from a node down to a leaf,
but the diameter is based on combining two heights — one from the left child and one from the right — to form the longest path through the current node.
'''

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)

            # Update max diameter at each node
            self.max_diameter = max(self.max_diameter, left + right)

            # Return height of current subtree
            return 1 + max(left, right)

        height(root)
        return self.max_diameter
