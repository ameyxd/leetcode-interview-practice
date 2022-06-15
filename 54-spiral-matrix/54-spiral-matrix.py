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
            
            # If after doing the first set ???
            if not  (left < right and top < bottom):
                break
            # if len(res) == len(matrix[0]) * len(matrix):
            #     break
            
            # get every i in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # get every i in the left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res
    

# Big idea: maintain the pointers to top, bottom, left and right and change them to make matrix smaller each time you traverse it completely
# Direction d should tell you which kind of movement to perform and updating d will be done such that d is incremented once and the modulo 4 so we keep going smaller and inward
# Range function needs to be carefully checked since the second arg is not inclusive
# While condition is to ensure we stop as soon as we have printed all elements

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        d = 0
        ans = []
        while (t <= b and l <= r):
            if (d == 0):
                for i in range(l, r+1):
                    ans.append(matrix[t][i])
                t+=1
            elif (d == 1):
                for i in range(t, b+1):
                    ans.append(matrix[i][r])
                r-=1
            elif (d == 2):
                for i in range(r, l-1, -1):
                    ans.append(matrix[b][i])
                b-=1
            elif (d == 3):
                for i in range(b, t-1, -1):
                    print(i)
                    ans.append(matrix[i][l])
                l+=1
            d = (d+1) % 4
            # print(t, b, l, r, d)
        return ans