class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # Sum everything in range and subtract original array's sum
        # n = len(nums)
        # res = n*(n+1)//2 - sum(nums)
        # return res
        
        # XOR Solution: We know XOR of number with itself is 0 and XOR of 0 with any number is the same number. So XOR the input list with the range in a loop
        
        xor_res = len(nums)
        for i, num in enumerate(nums):
            xor_res ^= i ^ num # res ^ i ^ i'th value
        
        return xor_res