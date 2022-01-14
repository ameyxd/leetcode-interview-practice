class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Strat: Sort list, pick a one by one, and apply left-right pointer technique from Two Sum II to get theb and c that sum to 0
        
        nums = sorted(nums)
        res = []
        
        for i, a in enumerate(nums):
            # Handle duplicates in first element (a)
            if i > 0 and a == nums[i - 1]:
                continue
            # Optimization: If first num of the three in sorted list is already positive then sum cannot be zero so return result
            if a > 0:
                return res
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[l] + nums[r] + a
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # Handle duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
    
    
        # Time complexity: O(nlogn) + O(n^2) = o(n^2)