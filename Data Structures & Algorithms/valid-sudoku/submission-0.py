class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        cols = 9

        # validate rows
        for i in range(rows):
            seen = set()

            for j in range(cols):
                val = board[i][j]

                if val == ".":
                    continue

                if val in seen:
                    return False

                seen.add(val)

        # validate cols
        for j in range(cols):
            seen = set()

            for i in range(rows):
                val = board[i][j]

                if val == ".":
                    continue

                if val in seen:
                    return False

                seen.add(val)

        # validate 3x3 boxes
        starts = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]

        for si, sj in starts:
            seen = set()

            for i in range(si, si + 3):
                for j in range(sj, sj + 3):
                    val = board[i][j]

                    if val == ".":
                        continue

                    if val in seen:
                        return False

                    seen.add(val)

        return True