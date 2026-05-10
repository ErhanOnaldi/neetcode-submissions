"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        oldToNew = {}
        q = deque()
        oldToNew[node] = Node(node.val)
        q.append(node)

        while q:
            processing = q.popleft()
            processingCopy = oldToNew[processing]
            for nei in processing.neighbors:
                if nei not in oldToNew:
                    neiCopy = Node(nei.val)
                    oldToNew[nei] = neiCopy
                    q.append(nei)
                if oldToNew[nei] not in processingCopy.neighbors:
                    processingCopy.neighbors.append(oldToNew[nei])
        
        return oldToNew[node]
                
