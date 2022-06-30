class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a number n is the start of a sequence when n - 1 is not present in the list
        longest = 0
        numSet = set(nums) # For efficient checking
        
        for num in nums:
            if num - 1 not in numSet: # start of new sequence
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
                
        return longest