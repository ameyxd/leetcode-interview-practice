class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        if ROWS == 1 or COLS == 1:
            return True
        r, c = 1, 1
        for row in range(r, ROWS):
            for col in range(c, COLS):
                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False
        return True