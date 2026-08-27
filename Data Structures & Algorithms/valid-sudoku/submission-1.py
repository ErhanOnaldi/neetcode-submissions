class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        cols = 9
        #validate rows
        for r in range(rows):
            s = set()
            for c in range(cols):
                current_element = board[r][c]
                if current_element == ".":
                    continue
                if current_element not in s:
                    s.add(current_element)
                else:
                    return False

        #validate cols
        for c in range(cols):
            s = set()
            for r in range(rows):
                current_element = board[r][c]
                if current_element == ".":
                    continue
                if current_element not in s:
                    s.add(current_element)
                else:
                    return False

        #validate 3x3 boxes
        start_points = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for point in start_points:
            x,y = point
            s = set()
            for r in range(x,x + 3):
                for c in range(y,y+3):
                    current_element = board[r][c]
                    if current_element == ".":
                        continue
                    if current_element not in s:
                        s.add(current_element)
                    else:
                        return False

        return True


                    
                