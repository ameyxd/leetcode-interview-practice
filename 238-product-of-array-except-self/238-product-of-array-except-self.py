class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        
        answer = [1] * len(nums)
        
        for i in range(len(nums)):
            answer[i] = prefix[i] * postfix[i]
        
        return answer
    
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
    # O(1) space solution
        answer = [1] * len(nums)
        prefix, postfix = 1, 1
        
        # Make answer array have prefixes first
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        # Then go through answer array in reverse and multiply the postfix
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer