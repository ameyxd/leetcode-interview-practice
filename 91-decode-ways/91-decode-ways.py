class Solution:
    def numDecodings1(self, s: str) -> int:
        # Brute force: (2^n) solution - branch every time you come across 1 and the next value is 0-9 or you come across a 2 and the next value is 0-6
        # DP: O(n) solution - Subproblem - how many ways can we decode a substring after i and use to calculate ways at i
        dp = {len(s): 1}
        
        # Recursive dfs solution
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0": # invalid
                return 0
            # if s[i] is 1-9
            res = dfs(i + 1)
            
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0) # # of ways starting at position 0
    
    # Iterative DP solution
    def numDecodings(self, s: str) -> int:
        # Brute force: (2^n) solution - branch every time you come across 1 and the next value is 0-9 or you come across a 2 and the next value is 0-6
        # DP: O(n) solution - Subproblem - how many ways can we decode a substring after i and use to calculate ways at i
        dp = {len(s): 1}
        
        for i in range(len(s) - 1, -1, -1):
            
            if s[i] == "0": # invalid
                dp[i] = 0
            # if s[i] is 1-9
            else:
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]

        return dp[0] # # of ways starting at position 0