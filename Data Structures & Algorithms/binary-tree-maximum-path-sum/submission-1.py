# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def dfs(node):
            nonlocal best
            if not node:
                return 0

            leftGain = max(0, dfs(node.left))
            rightGain = max(0, dfs(node.right))
            currentPath = node.val + leftGain + rightGain
            best = max(best, currentPath)

            return node.val + max(leftGain, rightGain)

        dfs(root)
        return best