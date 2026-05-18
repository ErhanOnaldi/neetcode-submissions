class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i,j):
            if i >= rows or i < 0 or j >= cols or j < 0:
                return
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            for dr,dc in directions:
                nr, nc = i + dr, j + dc
                dfs(nr,nc)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i,j)
    
        return islands
