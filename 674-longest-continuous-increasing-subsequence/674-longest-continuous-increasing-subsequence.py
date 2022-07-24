class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # sliding window approach
        res, beg = 0, 0
        # beg will be the beginning of the sliding window, and i will be the end
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] >= nums[i]:
                beg = i # only set new starting point of sliding window when you notice a decrease
            res = max(res, i - beg + 1)
        return res