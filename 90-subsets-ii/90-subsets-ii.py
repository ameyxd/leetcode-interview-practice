class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity = O(n*2^n)
        # Space Complexity = O(n)
        nums = sorted(nums) # will compare numbers for duplicate check
        res = []
        subset = []
        
        def backtrack(start):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i - 1]: # Since duplicate numbers may exist
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
                
        backtrack(0)
        return res