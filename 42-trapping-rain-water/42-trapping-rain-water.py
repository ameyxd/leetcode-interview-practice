class Solution:
    def trap(self, height: List[int]) -> int:
        # l, r = 0, len(nums) - 1
        # maxLeftH, maxRightH = height[l], height[r]
        
        maxLeft, maxRight = [0] * len(height), [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(height[i + 1], maxRight[i + 1])
        
        res = 0
        for i in range(len(height)):
            waterAti = min(maxLeft[i], maxRight[i]) - height[i]
            if waterAti > 0:
                res += waterAti
        return res