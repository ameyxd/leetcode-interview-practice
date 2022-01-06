class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if nums[mid] > nums[0]:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return left
        
        if len(nums) == 1: return nums[0]
        
        left, right = 0, len(nums) - 1
        
        if nums[right] > nums [0]:
            return nums[0]
        
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1] # This is where the inflection point is: min element
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid
        # return left