class Solution:
    # Same as binary search, catch is to return left pointer if element is not found
    def searchInsert1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
                
        
        # Better implementation like template
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) # Since search space needs to be one larger if target is greater than last element it will have to go in the end acc to question
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target: # condition: We need to find the min k value that satisfies nums[k] >= target
                right = mid
            else:
                left = mid + 1
        return left