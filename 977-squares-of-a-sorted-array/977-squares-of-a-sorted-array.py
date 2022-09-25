class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        sq = [0] * len(nums)
        
        # Start filling from end
        curr_pos = len(nums) - 1
        while left <= right:
            rightval, leftval = nums[right] ** 2, nums[left] ** 2
            if rightval > leftval:
                sq[curr_pos] = rightval
                right -= 1
            else:
                sq[curr_pos] = leftval
                left += 1
            curr_pos -= 1
            
        return sq