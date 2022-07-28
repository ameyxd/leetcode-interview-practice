class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        
        # Brute force
        ans = [[0] * n for _ in range(m)]
        for row in range(m):
            for i in range(k):
                # Optimization on brute force: don't calculate if mat1[row][i] is 0
                # Only iterate over the cols in mat2 if the value it is being multiplied to is non-zero
                if mat1[row][i]:
                    for col in range(n):
                        ans[row][col] += mat1[row][i] * mat2[i][col]       
        return ans