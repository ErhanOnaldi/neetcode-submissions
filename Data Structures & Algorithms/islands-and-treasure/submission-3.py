from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                  q.append((r,c))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        dist = 0
        while q:
            level = len(q)
            dist += 1
            for i in range(level):
                processingRow, processingCol = q.popleft()
                for dr, dc in directions:
                    nr, nc = processingRow + dr, processingCol + dc
                    if nr >= rows or nr < 0 or nc >= cols or nc < 0 or grid[nr][nc] != 2147483647:
                        continue
                    
                    grid[nr][nc] = dist
                    q.append((nr,nc))
                    
