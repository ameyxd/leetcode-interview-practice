class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Strat - think of when any number is the start of a sequence : when n - 1 is not present in the set
        # Use set data structure
        
        longest = 0
        numSet = set(nums)
        
        for n in nums:
            # Check if n - 1 is present in set : if not, that means n is the start of a new sequence
            if n - 1 not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest