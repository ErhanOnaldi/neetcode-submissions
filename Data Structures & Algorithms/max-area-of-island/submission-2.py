class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxArea = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i,j) -> int:
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            
            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            area = 1

            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                area += dfs(nr,nc)

            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(area,maxArea)
        return maxArea


