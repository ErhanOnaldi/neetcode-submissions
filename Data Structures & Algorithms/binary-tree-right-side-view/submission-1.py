# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []
        while q:
            length = len(q)
            level = []
            for _ in range(length):
                processing_node = q.popleft()
                level.append(processing_node.val)
                if processing_node.left: q.append(processing_node.left)
                if processing_node.right: q.append(processing_node.right)

            res.append(level)

        return [level[-1] for level in res]
        