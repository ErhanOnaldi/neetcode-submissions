class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i,j):
            if grid[i][j] == "0":
                return 
            grid[i][j] = "0"

            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0":
                    continue
                dfs(nr,nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        
        return islands
