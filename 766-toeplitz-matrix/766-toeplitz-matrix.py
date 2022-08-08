class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # A one row or one col matrix is a Toeplitz matrix
        if ROWS == 1 or COLS == 1:
            return True
        # Start from second row second column
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False
        return True