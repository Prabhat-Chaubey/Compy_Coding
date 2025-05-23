class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None

        def dfs(node):
            if node is None:
                return 0

            total = 0
            if isLeaf(node.left):  # Only add if the left child is a leaf
                total += node.left.val
            total += dfs(node.left)
            total += dfs(node.right)
            return total

        return dfs(root)
