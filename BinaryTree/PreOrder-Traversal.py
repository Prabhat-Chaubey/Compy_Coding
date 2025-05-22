# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        listval=[]
        if root:
            listval.append(root.val)
            listval=listval+self.preorderTraversal(root.left)
            listval=listval+self.preorderTraversal(root.right)
        return listval
        
