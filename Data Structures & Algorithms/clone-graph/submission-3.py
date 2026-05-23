from typing import Optional
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned_map = {}

        def dfs(curr_node):
            if curr_node in cloned_map:
                return cloned_map[curr_node]
            
            clone = Node(curr_node.val)
            cloned_map[curr_node] = clone
            
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone

        return dfs(node)