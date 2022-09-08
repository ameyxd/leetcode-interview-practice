class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for c in range(n)] for r in range(m)]
        
        dp[0][0] = 1
        for i in range(1, n):
            dp[0][i] = int(obstacleGrid[0][i] == 0 and dp[0][i - 1] == 1)
        
        for i in range(1, m):
            dp[i][0] = int(obstacleGrid[i][0] == 0 and dp[i - 1][0] == 1)
        
        # Skip when at obstacle
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        print(dp)
        return dp[-1][-1]