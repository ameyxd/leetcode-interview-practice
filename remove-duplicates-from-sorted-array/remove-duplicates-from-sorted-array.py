class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextNonDup, i = 0, 1
        while i < len(nums):
            if nums[i] != nums[nextNonDup]:
                nums[nextNonDup + 1] = nums[i]
                nextNonDup += 1
            i += 1
        return nextNonDup + 1
    
    # Strat: Two pointers: next non dup and i to iterate