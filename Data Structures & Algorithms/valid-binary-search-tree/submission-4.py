# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = [True]

        def dfs(node,lower_bound,upper_bound):
            if not node:
                return
            if not (node.val > lower_bound and node.val < upper_bound):
                isValid[0] = False
                return
            dfs(node.left,lower_bound,node.val)
            dfs(node.right,node.val,upper_bound)

        dfs(root,-1001, 1001)
        return isValid[0]

