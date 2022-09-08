class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # extra space
        # a = [0] * len(nums)
        # for i in range(len(nums)):
        #     a[(i + k) % len(nums)] = nums[i]
        # nums = a
        
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        pos = k % len(nums)
        # reverse first pos numbers
        # reverse pos + 1 numbers through end
        # return nums[:pos + 1][::-1] + nums[pos + 1:][::-1]
        
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, pos - 1)
        reverse(nums, pos, len(nums) - 1)
        # return nums