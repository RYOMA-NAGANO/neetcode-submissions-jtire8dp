class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, positiveDiagonal, negativeDiagonal = set(), set(), set()

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for col in range(n):
                if col in cols or (row + col) in positiveDiagonal or (row - col) in negativeDiagonal:
                    continue
                cols.add(col)
                positiveDiagonal.add(row + col)
                negativeDiagonal.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                positiveDiagonal.remove(row + col)
                negativeDiagonal.remove(row - col)
                board[row][col] = "."
        backtrack(0)
        return res
