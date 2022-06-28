class Solution:
        
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def rob_helper(i, nums):
            if i >= len(nums): return 0
            
            if i in memo: return memo[i]
            
            ans = max(rob_helper(i + 1, nums), rob_helper(i + 2, nums) + nums[i])
            memo[i] = ans
            return ans
        return rob_helper(0, nums)
        
    def rob_1(self, nums: List[int]) -> int:
        # Recurrence relationship: Either rob first house or rob second house: Break into subproblems
        # return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        
        # Going forward, so we can expect max(nums[i] + rob(nums[i - 2]), nums[i - 1])
        # [rob1, rob2, n, n+1]
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2