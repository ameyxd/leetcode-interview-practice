class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         # Calculate leftProduct and rightProduct arrays to keep track of product until before and after any point i, then multiply them together
        
#         prefix = [1] * len(nums)
#         postfix = [1] * len(nums)
                
#         for i in range(1, len(nums)):
#             prefix[i] = nums[i - 1] * prefix[i - 1]
        
#         for i in range(len(nums) - 2, -1, -1):
#             postfix[i] = postfix[i + 1] * nums[i + 1]
        
#         answer = [1] * len(nums)
        
#         for i in range(len(nums)):
#             answer[i] = prefix[i] * postfix[i]
        
#         return answer

#         # O(1) space solution:
        prefix, postfix = 1, 1
        ans = [1] * len(nums)
        
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans