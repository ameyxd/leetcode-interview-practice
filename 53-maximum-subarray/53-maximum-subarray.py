class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        
        # If the number you're looking at is greater than the sum of everything up to it, i.e. (current sum + n), then set the current sum to n, else add n to current ssum
        
        for n in nums:
            if n > currSum + n:
                currSum = n
            else:
                currSum += n
            maxSum = max(maxSum, currSum)
            
        return maxSum