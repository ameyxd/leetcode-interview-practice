class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)
    
    # choice of whether to include in LIS at position i or not
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)