class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i :[] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for nei in adj[node]:
                if nei == parent: 
                    continue
                if nei in visited: 
                    continue
                dfs(nei, node)

        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i,-1)
    
        return components