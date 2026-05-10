class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2) 
            adj[n2].append(n1) 
        
        visited = set()

        def dfs(node, parent) -> bool:
            visited.add(node)
            for nei in adj[node]:
                if nei == parent: 
                    continue
                if nei in visited: 
                    return True
                if dfs(nei, node): 
                    return True
            
            return False
        
        if dfs(0, -1):
            return False 
        
        if len(visited) != n:
            return False
        
        return True