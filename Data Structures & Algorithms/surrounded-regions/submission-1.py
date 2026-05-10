from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i,j):
            if i >= rows or i < 0 or j >= cols or j < 0:
                return
            if board[i][j] == "." or board[i][j] == "X":
                return
            
            board[i][j] = "."
            for dr,dc in directions:
                dfs(dr + i, dc + j)
            
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols - 1] == "O":
                dfs(r, cols -1)
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X" 
                elif board[r][c] == ".":
                    board[r][c] = "O" 