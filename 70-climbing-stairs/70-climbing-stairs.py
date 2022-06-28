class Solution:
    def __init__(self):
        self.memo = {}
        # DP Recursion with memoization O(n)
    def climbStairs1(self, n: int) -> int:
        if n == 0 or n == 1: return 1
        else:
            if n in self.memo:
                return self.memo[n]
            else:
                self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
                return self.memo[n]

    # DP: O(n) Space: O(n)
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
    
    # Fibonacci number Time: O(n) Space: O(1)
    def climbStairs2(self, n: int) -> int:
        if n == 1: return 1
        first = 1
        second = 2
        for i in range(3, n):
            third = first + second
            first = second
            second = third
        return second