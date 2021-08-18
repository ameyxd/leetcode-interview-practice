class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_nums = [0 for x in range(len(nums))]
        highest_sq_index = len(nums) - 1
        left, right = 0, len(nums) - 1
        while left <= right:
            right_sq_val = nums[right] ** 2
            left_sq_val = nums[left] ** 2
            if right_sq_val > left_sq_val:
                sq_nums[highest_sq_index] = right_sq_val
                right -= 1
            else:
                sq_nums[highest_sq_index] = left_sq_val
                left += 1
            highest_sq_index -= 1
        return sq_nums

    
    # Strat: Two pointers. Start one at start, one at end move one by one and add to squares list from end.