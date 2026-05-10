from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
                else:
                    continue
            
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0
        while q and fresh > 0:
            level = len(q)
            for _ in range(level):
                processingRow, processingCol = q.popleft()
                for dr, dc in directions:
                    nr, nc = processingRow + dr, processingCol + dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1





        return minutes if fresh <= 0 else -1 