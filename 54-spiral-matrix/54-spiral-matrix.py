class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # worry about first layer, internal layers are subproblems
        # set left, right, top and bottom boundaries
        # update boundaries as soon as that section is added to output
        # Time: O(m*n) Space: O(1)

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []
        
        while left < right and top < bottom:
            # get every i in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # get every i in right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            # if not  (left < right and top < bottom):
            #     break
            if len(res) == len(matrix[0]) * len(matrix):
                break
            
            # get every i in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # get every i in the left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res