''' 
### 📝 Shortened Approach:

We use a recursive bottom-up approach to find the maximum depth of a binary tree. For each node, we calculate the depth of its left and right subtrees,
then return `1 + max(left, right)`. If a node is `None`, we return `0`. This continues until the recursion unwinds back to the root, giving the tree's maximum depth.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)

        return 1+ max(left_depth,right_depth)

# hum recursion logic aise sochte ki abb , is node se kya hoga, left hieght milega , right milega , max of left ya right and +1 toh chahiye, bas abb ye hoga ki right and left age jate 
# rahega isliye wo recursion hai
