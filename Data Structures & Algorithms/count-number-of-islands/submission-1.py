class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            for dr, dc in directions:
                nr = dr + i
                nc = dc + j
                dfs(nr,nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1 
                    dfs(r,c)
        
        return islands