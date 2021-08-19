class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, product, result = 0, 1, 0
        for r in range(len(nums)):
            product *= nums[r]
            
            while product >= k and l <= r:
                product /= nums[l]
                l += 1
            
            result += r - l + 1
            
        return result
    
    
    # Strat: Sliding window with two pointers. 'Product' contains the product of the elements from l to r. As soon as the product becomes greater than target, we shift l until it doesn't. After every iteration, there are r - l + 1 potential subarrays to be added to result.