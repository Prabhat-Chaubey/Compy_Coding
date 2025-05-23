


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.right is None and root.left is None:
            return targetSum == root.val
        
        targetSum=targetSum-root.val
        leftpath=self.hasPathSum(root.left,targetSum)
        rightpath=self.hasPathSum(root.right,targetSum)
        
        return leftpath or rightpath
