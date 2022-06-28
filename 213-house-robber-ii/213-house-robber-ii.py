class Solution:
    def rob(self, nums: List[int]) -> int:
        # Problem breaks down into solving house robbers and getting max of stealing from house 2 to n, and from 1 to n - 1
        def helper(nums): # This helper function is the solution of house robber 1
            rob1, rob2 = 0, 0
            for house in nums:
                currRob = max(rob1 + house, rob2)
                rob1 = rob2
                rob2 = currRob
            return rob2
    
        return max(nums[0], helper(nums[1:]), helper(nums[:-1])) # nums[0] for when the input is only one element. 