class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        if len(cost) > 1:
            dp[1] = cost[1]
        
        # dp[2] = cost[2] + min(dp[1], dp[0])
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
            
        # Since you can reach the end n from n - 1 or n - 2
        return min(dp[-1], dp[-2])