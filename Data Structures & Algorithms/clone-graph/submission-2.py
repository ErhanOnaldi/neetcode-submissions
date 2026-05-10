"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        
        new_node = Node(node.val)
        node_clone_map = {node: new_node}

        def dfs(neighbor):
            if neighbor in node_clone_map:
                return node_clone_map[neighbor]
            
            new_node = Node(neighbor.val)
            node_clone_map[neighbor] = new_node
            for ne in neighbor.neighbors:
                new_node.neighbors.append(dfs(ne))
            return new_node
        
        for neighbor in node.neighbors:
            new_node.neighbors.append(dfs(neighbor))
        
        return new_node
                
