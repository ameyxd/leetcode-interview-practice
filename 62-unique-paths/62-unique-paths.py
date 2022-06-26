class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # use a cache to store at x the sum of R and D nodes
        # - R - - -
        # D x - - -
        
        # DP: start from paths to get to finish from the finish and move toward start
        # base case: how many paths to get to finish from finish = 1

        res = [[0] * n for _ in range(m)] # Create cache/grid of size (m) * (n)
        for i in range(n):
            res[m - 1][i] = 1
        for j in range(m):
            res[j][n - 1] = 1

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                res[r][c] = res[r + 1][c] + res[r][c + 1]
        return res[0][0]
    
    # Math based solution: [(n - 1) + (m - 1)] C (n - 1) # Choosing where the right/left moves go