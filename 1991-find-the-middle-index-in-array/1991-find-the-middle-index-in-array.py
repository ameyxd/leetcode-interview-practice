class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        total = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            if leftSum == total - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        return -1