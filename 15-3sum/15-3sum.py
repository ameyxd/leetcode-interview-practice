class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            # handle duplicates in start
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Optimization: if the first num of the three in sorted array is positive, return result since no combination after that will sum to 0
            if nums[i] > 0:
                return res
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    
                    # Handle duplicates when j moves
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    
                elif threesum > 0:
                    k -= 1
                else:
                    j += 1
        return res