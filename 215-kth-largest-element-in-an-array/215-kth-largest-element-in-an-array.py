class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Simple solution: Sort and give out n - kth value - O(nlogn)
        # nums.sort()
        # return nums[len(nums) - k]
        
        # Quickselect algorithm
        # (In sorted array, we need the kth largest)
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p] # Swap pivot with nums[p]
            
            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]
        
        return quickSelect(0, len(nums) - 1)