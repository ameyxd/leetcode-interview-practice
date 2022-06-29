class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Brute force - dfs backtracking: n choices in decision tree
        # Repeating subproblems - make tree diagram
        # Time: O(amount * len(coins))
        # Memory: O(amount))
        
        MAX_INT = float("inf") # You can use amount + 1 instead of float inf
        dp = [MAX_INT] * (amount + 1) 
        dp[0] = 0 # min number of coins to sum to 0
        # dp[1] = # min number of coins to sum to 1
        
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    # We can continue searching
                    dp[a] = min(dp[a], 1 + dp[a - coin]) # eg coin = 4, a = 7, then dp[7] = 1 + dp[7 - 4]
        
        return dp[amount] if dp[amount] != MAX_INT else -1