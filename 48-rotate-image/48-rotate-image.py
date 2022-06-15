class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time: O(n^2) only look at matrix once, Space O(1) no extra memory
        # Only worry about first layer, the inner layers are subproblems
        
        # If you do reversal in counterclockwise direction, you only need one variable
        l, r = 0, len(matrix) - 1
        
        while l < r:
            # First write code without i, then include i because you need to do the rotation by moving l -> l + 1 and so on, use a 4x4 grid as example and see how movement occurs using arrows
            for i in range(r - l): # number of rotations to do will be r - l, like in example 2: moving 5, then moving 1, then moving 9. In the smaller matrix, moving 4
                top, bottom = l, r
                # save top left
                topLeft = matrix[top][l + i]
                
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # move top left into top right
                matrix[top + i][r] = topLeft
                
            r -= 1
            l += 1
            
        
#         # Another solution can be simply to transpose and reverse rows
#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 temp = matrix[row][col]
#                 matrix[row][col] = matrix[col][row]
#                 matrix[col][row] = temp
        
#         for row in matrix:
#             row.reverse()