class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Brute force - making a copy of the array and updating the values in it does repeated work and takes O(m*n) time and O(m*n) space
        # Instead, use O(m + n) space to only have one list to indicate which rows to set to 0, and one list to indicate which cols to set to 0
        # For constant space complexity O(1)
        
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        
        # Determine which rows and cols need to be zero
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # set first row in that col to 0
                    matrix[0][c] = 0
                    # set first col in that row to 0, but only if r > 0, because for row zero we have a dedicated value rowZero
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # If first row or column is to be set to 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Zero out first column if needed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # Zero out first row if you need to
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0