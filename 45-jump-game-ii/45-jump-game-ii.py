class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        # What portion to use for BFS
        left, right = 0, 0
        
        # Simplified BFS on 1D array
        while right < len(nums) - 1: # after each loop, left will be set to right + 1, and right will be set to the farthest index that can be reached
            farthest = 0            
            for i in range(left, right + 1): # farthest jump that can be made 
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            res += 1
        return res