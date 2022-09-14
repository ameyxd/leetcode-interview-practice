class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if text1[r] == text2[c]:
                    dp[r + 1][c + 1] = 1 + dp[r][c]
                else:
                    dp[r + 1][c + 1] = max(dp[r + 1][c], dp[r][c + 1])
                
                
        return dp[-1][-1]