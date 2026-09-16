class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRow, firstCol = False, False
        ROWS, COLS = len(matrix), len(matrix[0])
        for c in range(COLS):
            if matrix[0][c] == 0:
                firstRow = True
        
        for r in range(ROWS):
            if matrix[r][0] == 0:
                firstCol = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if firstRow:
            for c in range(COLS):
                matrix[0][c] = 0
        
        if firstCol:
            for r in range(ROWS):
                matrix[r][0] = 0

        