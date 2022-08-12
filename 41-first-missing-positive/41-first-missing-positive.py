class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Only 1 to n matter
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            # Place nums[i] in the correct position if nums[i] is in the range[1, n]
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        # All integers that could be placed at the right index will be placed, find the index that is occupied incorrectly
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1