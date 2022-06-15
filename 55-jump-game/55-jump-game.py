class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Brute force will be finding each path down a tree : O(n^n)
        # Greedy solution : O(n)
        # Think in reverse, if you can get to the end from a point to its left, that means you just need to be able to get to that point
        # in [2, 3, 1, 1, 4] if you can get to 4 from 1, then you just need to get to 1 and so on
        
        goalPost = len(nums) - 1
        
        # work our way backwards
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goalPost: # if making jump of (nums[i]) from i takes us to or beyond the goalpost, we can shift goalpost backward
                goalPost = i
        # either goal will be 0 or > 0
        return goalPost == 0
    
        # #Same solution but moving forward instead: I found the backward pass more intuitive than this one
        # reach = 0
        # for i in range(len(nums)):
        #     if i + nums[i] > reach: # If I make a jump from ith position to a new position, add to reach
        #         reach = i
        # return reach >= len(nums) - 1