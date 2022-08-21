class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)))
        # One pass
        inc = dec = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                inc = False
            if nums[i] < nums[i + 1]:
                dec = False
        return inc or dec